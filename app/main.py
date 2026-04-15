from __future__ import annotations

from datetime import date, datetime, time

import streamlit as st

from app.constants import (
    CARGO_TYPES,
    CORRIDOR_OCEAN,
    GEOPOLITICAL_RISK_OPTIONS,
    PORT_REGION,
    PORT_RISK_OPTIONS,
    RISK_LABEL_TO_LEVEL,
    SCENARIOS,
    VESSEL_TYPES,
    WEATHER_RISK_OPTIONS,
)
from app.data_utils import find_default_option_by_risk, infer_distance_and_eta, load_data
from app.layout import render_hero, render_page_style
from app.modeling import add_time_features, build_model_input, format_delay_class, load_models
from app.visuals import build_delay_gauge, build_world_map


def run_app() -> None:
    # Expose symbol in __main__ for joblib pickle compatibility.
    _ = add_time_features

    st.set_page_config(
        page_title="ChainPulse AI - Route Simulator",
        page_icon="🌍",
        layout="wide",
    )

    render_page_style()
    render_hero()

    try:
        dataset = load_data()
        models = load_models()
    except Exception as exc:
        st.error(
            "Could not load models or dataset. "
            "Check that .joblib artifacts exist in models/app_ready and the CSV is in data/processed."
        )
        st.exception(exc)
        st.stop()

    all_ports = sorted(PORT_REGION.keys())
    corridor_options = sorted(CORRIDOR_OCEAN.keys())

    left, right = st.columns([1.2, 1.1], gap="large")

    with left:
        st.subheader("1) Configure the shipment")

        scenario_name = st.selectbox("Quick mode", options=list(SCENARIOS.keys()), index=0)
        scenario = SCENARIOS[scenario_name]

        origin_port = st.selectbox("Origin port", options=all_ports, index=7)
        destination_port = st.selectbox("Destination port", options=all_ports, index=2)

        if destination_port == origin_port:
            st.warning("Origin and destination are the same, which may produce unrealistic simulations.")

        route_corridor = st.selectbox("Route corridor", options=corridor_options, index=2)
        ocean_side = CORRIDOR_OCEAN[route_corridor]
        st.caption(f"Suggested ocean side: {ocean_side}")

        vessel_type = st.selectbox("Vessel type", options=VESSEL_TYPES, index=1)
        cargo_type = st.selectbox("Cargo type", options=CARGO_TYPES, index=2)

        departure_date = st.date_input("Departure date", value=date.today())
        departure_hour = st.slider("Departure hour", min_value=0, max_value=23, value=9)

        suggested_distance, suggested_eta = infer_distance_and_eta(
            dataset, origin_port, destination_port, route_corridor
        )

        with st.expander("Advanced adjustments (optional)"):
            distance_nm = st.number_input(
                "Voyage distance (nautical miles)",
                min_value=100.0,
                max_value=20000.0,
                value=round(suggested_distance, 1),
                step=50.0,
            )
            baseline_eta_days = st.number_input(
                "Baseline ETA (days)",
                min_value=1.0,
                max_value=120.0,
                value=round(suggested_eta, 2),
                step=0.5,
            )

        st.subheader("2) Adjust risk settings")

        weather_default = find_default_option_by_risk(WEATHER_RISK_OPTIONS, scenario["weather"])
        weather_options = list(WEATHER_RISK_OPTIONS.keys())
        weather_option = st.selectbox(
            "Weather condition",
            options=weather_options,
            index=weather_options.index(weather_default),
        )
        weather_label = str(WEATHER_RISK_OPTIONS[weather_option]["risk"])
        st.caption(f"Applied level: {weather_label}. {WEATHER_RISK_OPTIONS[weather_option]['description']}")

        port_default = find_default_option_by_risk(PORT_RISK_OPTIONS, scenario["port"])
        port_options = list(PORT_RISK_OPTIONS.keys())
        port_option = st.selectbox(
            "Port status",
            options=port_options,
            index=port_options.index(port_default),
        )
        port_label = str(PORT_RISK_OPTIONS[port_option]["risk"])
        st.caption(f"Applied level: {port_label}. {PORT_RISK_OPTIONS[port_option]['description']}")

        geo_default = find_default_option_by_risk(GEOPOLITICAL_RISK_OPTIONS, scenario["geo"])
        geo_options = list(GEOPOLITICAL_RISK_OPTIONS.keys())
        geo_option = st.selectbox(
            "Geopolitical event by location",
            options=geo_options,
            index=geo_options.index(geo_default),
        )
        geo_config = GEOPOLITICAL_RISK_OPTIONS[geo_option]
        geo_label = str(geo_config["risk"])
        st.caption(f"Applied level: {geo_label}. {geo_config['description']}")

        if geo_option != "No relevant incident":
            route_match = route_corridor in geo_config["corridors"]
            origin_region = PORT_REGION[origin_port]
            destination_region = PORT_REGION[destination_port]
            region_match = origin_region in geo_config["regions"] or destination_region in geo_config["regions"]

            if route_match or region_match:
                st.warning("This geopolitical event is relevant to the selected route. Impact can be significant.")
            else:
                st.info("This geopolitical event has low relevance for the selected route.")

        run_prediction = st.button("Predict route impact", type="primary", use_container_width=True)

    with right:
        st.subheader("3) Map and predictions")

        if run_prediction:
            departure_dt = datetime.combine(departure_date, time(hour=departure_hour))
            payload = build_model_input(
                departure_dt=departure_dt,
                origin_port=origin_port,
                destination_port=destination_port,
                route_corridor=route_corridor,
                ocean_side=ocean_side,
                vessel_type=vessel_type,
                cargo_type=cargo_type,
                distance_nm=distance_nm,
                baseline_eta_days=baseline_eta_days,
                weather_risk_level=RISK_LABEL_TO_LEVEL[weather_label],
                port_congestion_level=RISK_LABEL_TO_LEVEL[port_label],
                geopolitical_risk_level=RISK_LABEL_TO_LEVEL[geo_label],
            )

            expected_delay = float(models["expected_delay_days"].predict(payload)[0])
            adjusted_eta = float(models["adjusted_eta_days"].predict(payload)[0])
            freight_index = float(models["freight_cost_index"].predict(payload)[0])
            delay_class = str(models["delay_class"].predict(payload)[0])

            c1, c2 = st.columns(2)
            with c1:
                st.metric("Expected delay", f"{expected_delay:.2f} days")
                st.metric("Delay class", format_delay_class(delay_class))
            with c2:
                st.metric("Adjusted ETA", f"{adjusted_eta:.2f} days")
                st.metric("Freight cost index", f"{freight_index:.3f}")

            if delay_class == "critical_delay":
                st.error("High risk of critical delay for this configuration.")
            elif delay_class == "minor_delay":
                st.warning("Scenario indicates a tendency for minor delay.")
            else:
                st.success("Route has a good chance of staying on time.")

            fig = build_world_map(
                origin=origin_port,
                destination=destination_port,
                delay_class=delay_class,
                expected_delay_days=expected_delay,
                freight_cost_index=freight_index,
            )
            st.plotly_chart(fig, use_container_width=True)

            gauge = build_delay_gauge(delay_class=delay_class, expected_delay=expected_delay)
            st.plotly_chart(gauge, use_container_width=True)
        else:
            st.info("Fill in the controls and click Predict route impact to generate results.")


if __name__ == "__main__":
    run_app()
