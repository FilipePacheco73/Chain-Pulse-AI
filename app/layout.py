from __future__ import annotations

import streamlit as st


def render_page_style() -> None:
    st.markdown(
        """
        <style>
          .stApp {
            background: radial-gradient(circle at 0% 0%, #f3eee3 0%, #f8f7f4 45%, #e6eef7 100%);
          }
          .kpi-card {
            border-radius: 14px;
            border: 1px solid #e3dfd2;
            background: #fffdf8;
            padding: 14px;
          }
          .hero {
            padding: 14px 16px;
            border-radius: 14px;
            background: linear-gradient(105deg, #13293d 0%, #1f4e79 60%, #2f7ca8 100%);
            color: white;
          }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    st.markdown(
        """
        <div class="hero" style="padding:10px 16px;">
          <span style="font-size:1.15rem;font-weight:700;">ChainPulse AI &mdash; Maritime Route Simulator</span>
          <span style="font-size:0.85rem;margin-left:12px;opacity:0.85;">Choose a scenario, adjust inputs, and get ETA · delay · freight predictions in real time.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
