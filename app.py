import streamlit as st
import pandas as pd
import numpy as np

# Seiten-Konfiguration
st.set_page_config(page_title="TCG Predictor", page_icon="🃏", layout="centered")

st.title("🃏 TCG Card Scanner & Price Predictor")
st.write("Scanne deine Trading Card, um den aktuellen Wert und eine KI-Preisvorhersage zu sehen.")

# 1. Kamera-Scanner
st.subheader("📸 1. Karte scannen")
picture = st.camera_input("Halte die Karte in die Kamera und klicke auf 'Take Photo'")

if picture:
    st.success("Bild erfolgreich aufgenommen!")
    st.image(picture, caption="Deine Karte", width=300)
    
    # Hier kommt später die Bilderkennungs-KI hin
    st.info("🔍 Analysiere Karte... (Dummy: Glurak Holo - Base Set erkannt)")
    
    st.divider()

    # 2. Historische Daten (Dummy-Daten für den Start)
    st.subheader("📈 2. Preisentwicklung (Letzte 6 Monate)")
    
    # Wir generieren Test-Daten
    dates = pd.date_range(start="2025-11-01", periods=6, freq="ME")
    prices = [120, 125, 118, 130, 145, 140]
    
    df = pd.DataFrame({"Datum": dates, "Preis (€)": prices})
    st.line_chart(df.set_index("Datum"))

    st.divider()

    # 3. Vorhersage (Platzhalter für TimesFM)
    st.subheader("🤖 3. KI-Vorhersage (Nächste 3 Monate)")
    st.write("Google TimesFM berechnet den Trend...")
    
    # Dummy-Vorhersage-Daten
    future_dates = pd.date_range(start="2026-05-01", periods=3, freq="ME")
    future_prices = [142, 148, 155]
    
    df_future = pd.DataFrame({"Datum": future_dates, "Vorhersage (€)": future_prices})
    st.bar_chart(df_future.set_index("Datum"))
    
    st.metric(label="Erwarteter Wert in 3 Monaten", value="155,00 €", delta="+ 15,00 €")
