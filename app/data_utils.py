from __future__ import annotations

import pandas as pd
import streamlit as st

from app.constants import DATA_PATH


@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


def infer_distance_and_eta(
    data: pd.DataFrame,
    origin: str,
    destination: str,
    corridor: str,
) -> tuple[float, float]:
    same_pair = data[(data["origin_port"] == origin) & (data["destination_port"] == destination)]
    if not same_pair.empty:
        return (
            float(same_pair["distance_nm"].median()),
            float(same_pair["baseline_eta_days"].median()),
        )

    same_corridor = data[data["route_corridor"] == corridor]
    if not same_corridor.empty:
        return (
            float(same_corridor["distance_nm"].median()),
            float(same_corridor["baseline_eta_days"].median()),
        )

    return (
        float(data["distance_nm"].median()),
        float(data["baseline_eta_days"].median()),
    )


def find_default_option_by_risk(options: dict[str, dict[str, object]], target_risk: str) -> str:
    for option_name, config in options.items():
        if str(config["risk"]) == target_risk:
            return option_name
    return next(iter(options.keys()))
