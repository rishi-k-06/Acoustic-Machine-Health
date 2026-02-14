import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(page_title="Machine Sound Lab", page_icon="🔊", layout="wide")

st.title("🔊 Acoustic Predictive Maintenance")

if 'spectral_data' not in st.session_state:
    st.session_state.spectral_data = pd.DataFrame(columns=['Freq', 'Amplitude'])

placeholder = st.empty()

for _ in range(100):
    # Simulated FFT Data from Pico
    freqs = np.linspace(20, 20000, 100)
    amps = np.random.normal(0.1, 0.05, 100)
    
    # Simulate a "Bearing Failure" spike at 5kHz
    if _ > 50:
        amps[25] = 0.8 

    with placeholder.container():
        m1, m2 = st.columns(2)
        health_score = 100 - (max(amps) * 100)
        m1.metric("Machine Health Score", f"{round(health_score)}%", delta="-15%" if health_score < 70 else "Stable")
        m2.metric("Peak Frequency", "5.2 kHz" if max(amps) > 0.5 else "Baseline")

        if health_score < 75:
            st.error("🚨 PREDICTIVE ALERT: High-frequency anomaly detected in Motor Housing A.")

        fig = go.Figure(data=go.Scatter(x=freqs, y=amps, fill='tozeroy', line_color='cyan'))
        fig.update_layout(title="Live Acoustic Spectrum (Hz vs Magnitude)", 
                          xaxis_title="Frequency (Hz)", yaxis_title="Magnitude")
        st.plotly_chart(fig, use_container_width=True)
        
    time.sleep(1)
