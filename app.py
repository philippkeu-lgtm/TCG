import streamlit as st
import google.generativeai as genai

st.title("🛠️ API Debugger")

try:
    # Key laden
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    st.success("✅ API Key erfolgreich geladen!")
    
    st.subheader("Verfügbare Bild-Modelle für deinen Key:")
    
    # Alle Modelle abfragen
    models = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            models.append(m.name)
            
    # Liste anzeigen
    st.write(models)

except Exception as e:
    st.error(f"Fehler beim Verbinden: {e}")
