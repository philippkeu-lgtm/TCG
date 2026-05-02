import streamlit as st
import pandas as pd
import numpy as np
import google.generativeai as genai
from PIL import Image

# Seiten-Konfiguration
st.set_page_config(page_title="TCG Predictor", page_icon="🃏", layout="centered")

# API Key laden und KI konfigurieren
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Wir nutzen Gemini Flash, da es rasend schnell ist
    model = genai.GenerativeModel('gemini-1.5-pro-latest') 
except Exception as e:
    st.error("⚠️ API Key nicht gefunden. Bitte in den Streamlit Secrets eintragen!")

st.title("🃏 TCG Card Scanner & Price Predictor")
st.write("Scanne deine Trading Card, um den aktuellen Wert und eine KI-Preisvorhersage zu sehen.")

# 1. Kamera-Scanner
st.subheader("📸 1. Karte scannen")
picture = st.camera_input("Halte die Karte in die Kamera und klicke auf 'Take Photo'")

if picture:
    st.image(picture, caption="Gescanntes Bild", width=300)
    
    # Bild für die KI vorbereiten
    img = Image.open(picture)
    
    with st.spinner("🔍 Analysiere Karte mit KI..."):
        try:
            # Das ist die Anweisung an die KI
            prompt = "Du bist ein Experte für Trading Cards (Pokémon, Yu-Gi-Oh, Magic etc.). Analysiere dieses Bild. Antworte nur mit dem exakten Namen der Karte, dem Set (falls erkennbar) und Besonderheiten (z.B. Holo). Halte dich extrem kurz."
            
            # KI nach dem Ergebnis fragen
            response = model.generate_content([prompt, img])
            card_name = response.text.strip()
            
            st.success(f"**Erkannte Karte:** {card_name}")
        except Exception as e:
            st.error(f"Fehler bei der Bilderkennung: {e}")
            
    st.divider()

    # 2. Historische Daten (Dummy-Daten für den Start)
    st.subheader("📈 2. Preisentwicklung (Letzte 6 Monate)")
    
    dates = pd.date_range(start="2025-11-01", periods=6, freq="ME")
    prices = [120, 125, 118, 130, 145, 140]
    df = pd.DataFrame({"Datum": dates, "Preis (€)": prices})
    st.line_chart(df.set_index("Datum"))

    st.divider()

    # 3. Vorhersage (Platzhalter für TimesFM)
    st.subheader("🤖 3. KI-Vorhersage (Nächste 3 Monate)")
    st.write("Google TimesFM berechnet den Trend...")
    
    future_dates = pd.date_range(start="2026-05-01", periods=3, freq="ME")
    future_prices = [142, 148, 155]
    df_future = pd.DataFrame({"Datum": future_dates, "Vorhersage (€)": future_prices})
    st.bar_chart(df_future.set_index("Datum"))
    
    st.metric(label="Erwarteter Wert in 3 Monaten", value="155,00 €", delta="+ 15,00 €")
