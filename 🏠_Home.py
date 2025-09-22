# 🏠_Home.py
import streamlit as st

st.set_page_config(
    page_title="PunjabSim",
    page_icon="🌾",
    layout="wide"
)

# --- THEME TOGGLE ---
# This code block should be at the top of every page in your app

# Initialize session state for theme if it doesn't exist
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Define CSS for light and dark themes
light_theme_css = """
<style>
    .stApp { background-color: #FFFFFF; color: #000000; }
    .stSidebar { background-color: #F0F2F6; }
</style>
"""

dark_theme_css = """
<style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .stSidebar { background-color: #1c1c1c; }
    .stMetric_container { color: #FFFFFF; }
</style>
"""

# Button to toggle theme
if st.sidebar.button(f"Switch to {'Dark' if st.session_state.theme == 'light' else 'Light'} Mode"):
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Apply the selected theme's CSS
st.markdown(dark_theme_css if st.session_state.theme == "dark" else light_theme_css, unsafe_allow_html=True)
# --- THEME TOGGLE (PASTE THE ENTIRE BLOCK HERE) ---
if "theme" not in st.session_state:
    st.session_state.theme = "light"
# ... (rest of the theme code block) ...
st.markdown(dark_theme_css if st.session_state.theme == "dark" else light_theme_css, unsafe_allow_html=True)
# --- END OF THEME TOGGLE BLOCK ---

st.title("Welcome to PunjabSim! 🌾")
st.title("Welcome to PunjabSim! 🌾")
st.markdown("---")
st.subheader("Your AI-Powered Agricultural Decision Support System for Punjab")

st.markdown("""
PunjabSim is an interactive tool designed to help you understand the complex agricultural ecosystem of Punjab.
Navigate through the different sections using the sidebar on the left.

### Features:
- **Simulation Dashboard:** Tweak economic and environmental variables to see their impact on crop yield, farmer income, and the water table.
- **AI Crop Suggestion Bot:** Get intelligent crop recommendations based on soil type, water availability, and market trends.

Select a page from the sidebar to get started!
""")
st.info("This application is a prototype. All models are trained on simplified, mock data.")