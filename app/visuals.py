from __future__ import annotations

import plotly.graph_objects as go

from app.constants import DELAY_COLORS, PORT_COORDS


def build_world_map(
    origin: str,
    destination: str,
    delay_class: str,
    expected_delay_days: float,
    freight_cost_index: float,
) -> go.Figure:
    o_lat, o_lon = PORT_COORDS[origin]
    d_lat, d_lon = PORT_COORDS[destination]

    color = DELAY_COLORS.get(delay_class, "#3366cc")
    width = max(1.5, min(8.0, expected_delay_days + 1.2))
    marker_size = max(10.0, min(28.0, 10.0 + (freight_cost_index - 1.0) * 20.0))

    fig = go.Figure()

    fig.add_trace(
        go.Scattergeo(
            lon=[o_lon, d_lon],
            lat=[o_lat, d_lat],
            mode="lines",
            line={"width": width, "color": color},
            opacity=0.9,
            name="Predicted route",
        )
    )

    fig.add_trace(
        go.Scattergeo(
            lon=[o_lon, d_lon],
            lat=[o_lat, d_lat],
            mode="markers+text",
            text=[f"Origin: {origin}", f"Destination: {destination}"],
            textposition=["top center", "bottom center"],
            marker={"size": [marker_size, marker_size], "color": ["#0d6efd", color]},
            name="Ports",
        )
    )

    fig.update_geos(
        projection_type="natural earth",
        showcountries=True,
        showcoastlines=True,
        coastlinecolor="#666",
        countrycolor="#aaa",
        showland=True,
        landcolor="#f3efe2",
        showocean=True,
        oceancolor="#dbe9f4",
    )

    fig.update_layout(
        margin={"l": 0, "r": 0, "t": 20, "b": 0},
        height=430,
        paper_bgcolor="#f8f7f4",
        plot_bgcolor="#f8f7f4",
    )

    return fig


def build_delay_gauge(delay_class: str, expected_delay: float) -> go.Figure:
    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=max(0.0, min(3.0, expected_delay)),
            number={"suffix": " days"},
            title={"text": "Delay intensity"},
            gauge={
                "axis": {"range": [0, 3]},
                "bar": {"color": DELAY_COLORS.get(delay_class, "#3366cc")},
                "steps": [
                    {"range": [0, 1], "color": "#d5f5e3"},
                    {"range": [1, 2], "color": "#fdebd0"},
                    {"range": [2, 3], "color": "#fadbd8"},
                ],
            },
        )
    )
    gauge.update_layout(height=260, margin={"l": 20, "r": 20, "t": 40, "b": 10})
    return gauge
