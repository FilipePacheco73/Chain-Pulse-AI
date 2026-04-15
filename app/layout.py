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
        <div class="hero">
          <h2 style="margin:0;">ChainPulse AI - Maritime Route Simulator</h2>
          <p style="margin:6px 0 0 0;">Choose a scenario, adjust the inputs, and see ETA, delay, and freight cost predictions in real time.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
