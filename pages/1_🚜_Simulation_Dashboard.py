# pages/1_🚜_Simulation_Dashboard.py
import streamlit as st
import pandas as pd
import joblib
# --- THEME TOGGLE ---
# This code block should be at the top of every page in your app

# Initialize session state for theme if it doesn't exist
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Define CSS for light and dark themes
light_theme_css = """
<style>
    .stApp { background-color: #FFFFFF; color: #000000; }s
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

# Page title and introduction
st.title("🚜 Simulation Dashboard")
st.markdown("Adjust the variables to simulate agricultural outcomes.")

# --- Load Models (same as before) ---
@st.cache_resource
def load_models():
    yield_model = joblib.load('models/yield_model.pkl')
    water_model = joblib.load('models/water_model.pkl')
    return yield_model, water_model

yield_model, water_model = load_models()

# --- Sidebar Controls with Tooltips ---
st.sidebar.header("Simulation Controls")

rainfall = st.sidebar.slider(
    "Monsoon Rainfall (mm)", 300, 800, 550,
    help="Adjust the total millimeters of rainfall during the monsoon season."
)
msp = st.sidebar.slider(
    "Wheat MSP (₹ per Quintal)", 2000, 3500, 2275,
    help="Set the Minimum Support Price offered by the government."
)
subsidy = st.sidebar.slider(
    "Electricity Subsidy (%)", 50, 100, 90,
    help="Set the percentage of subsidy on electricity for water pumps."
)
fertilizer_cost = st.sidebar.slider(
    "Fertilizer Cost (₹ per bag)", 250, 1000, 500,
    help="Adjust the cost of a standard bag of fertilizer."
)

# --- Simulation Logic (same as before) ---
input_data_yield = pd.DataFrame([[rainfall, msp]], columns=['rainfall_mm', 'msp_price'])
input_data_water = pd.DataFrame([[rainfall, subsidy]], columns=['rainfall_mm', 'electricity_subsidy_%'])
predicted_yield = yield_model.predict(input_data_yield)[0]
predicted_water_drop = water_model.predict(input_data_water)[0]
total_cost = 75000 + (fertilizer_cost * 2) 
farmer_income = (predicted_yield * 10 * msp) - total_cost

# --- Display Dashboard (same as before) ---
st.subheader("Simulated Outcomes")
col1, col2, col3 = st.columns(3)
col1.metric("Predicted Yield", f"{predicted_yield:.2f} T/ha", f"{(predicted_yield-5.5):.2f}")
col2.metric("Estimated Farmer Income", f"₹ {int(farmer_income):,}", f"{(farmer_income-150000):.2f}")
col3.metric("Water Table Drop", f"{predicted_water_drop:.2f} m", f"{(predicted_water_drop-5):.2f}")

# --- NEW: Export Report Feature ---
st.markdown("---")
st.subheader("Export Simulation Report")

report_text = f"""
## PunjabSim Simulation Report

### Input Parameters:
- Monsoon Rainfall: {rainfall} mm
- Wheat MSP: ₹{msp} / Quintal
- Electricity Subsidy: {subsidy}%
- Fertilizer Cost: ₹{fertilizer_cost} / bag

### Predicted Outcomes:
- Predicted Yield: {predicted_yield:.2f} Tonnes/ha
- Estimated Farmer Income: ₹{int(farmer_income):,}
- Water Table Drop: {predicted_water_drop:.2f} meters
"""

if st.button("Generate Report"):
    st.text_area("Copy Your Report", report_text, height=300)
    st.download_button("Download Report as TXT", report_text, file_name="punjabsim_report.txt")
