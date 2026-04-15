from __future__ import annotations

from datetime import datetime

import joblib
import pandas as pd
import streamlit as st

from app.constants import MODEL_DIR, PORT_REGION


def add_time_features(frame: pd.DataFrame) -> pd.DataFrame:
    # Required by the serialized sklearn pipeline (FunctionTransformer)
    enriched = frame.copy()
    departure_ts = pd.to_datetime(enriched["departure_timestamp"], errors="coerce")
    enriched["departure_month"] = departure_ts.dt.month.fillna(0).astype(int)
    enriched["departure_dayofweek"] = departure_ts.dt.dayofweek.fillna(0).astype(int)
    enriched["departure_hour"] = departure_ts.dt.hour.fillna(0).astype(int)
    return enriched.drop(columns=["departure_timestamp"])


@st.cache_resource
def load_models() -> dict[str, object]:
    return {
        "expected_delay_days": joblib.load(f"{MODEL_DIR}/expected_delay_days_pipeline.joblib"),
        "adjusted_eta_days": joblib.load(f"{MODEL_DIR}/adjusted_eta_days_pipeline.joblib"),
        "freight_cost_index": joblib.load(f"{MODEL_DIR}/freight_cost_index_pipeline.joblib"),
        "delay_class": joblib.load(f"{MODEL_DIR}/delay_class_pipeline.joblib"),
    }


def format_delay_class(label: str) -> str:
    pretty = {
        "on_time": "On time",
        "minor_delay": "Minor delay",
        "critical_delay": "Critical delay",
    }
    return pretty.get(label, label)


def build_model_input(
    departure_dt: datetime,
    origin_port: str,
    destination_port: str,
    route_corridor: str,
    ocean_side: str,
    vessel_type: str,
    cargo_type: str,
    distance_nm: float,
    baseline_eta_days: float,
    weather_risk_level: int,
    port_congestion_level: int,
    geopolitical_risk_level: int,
) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "departure_timestamp": departure_dt.strftime("%Y-%m-%d %H:%M:%S"),
                "origin_port": origin_port,
                "destination_port": destination_port,
                "origin_region": PORT_REGION[origin_port],
                "destination_region": PORT_REGION[destination_port],
                "route_corridor": route_corridor,
                "ocean_side": ocean_side,
                "vessel_type": vessel_type,
                "cargo_type": cargo_type,
                "distance_nm": float(distance_nm),
                "baseline_eta_days": float(baseline_eta_days),
                "weather_risk_level": int(weather_risk_level),
                "port_congestion_level": int(port_congestion_level),
                "geopolitical_risk_level": int(geopolitical_risk_level),
            }
        ]
    )
