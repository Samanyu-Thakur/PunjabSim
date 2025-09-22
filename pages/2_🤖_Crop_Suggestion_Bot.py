# pages/2_🤖_Crop_Suggestion_Bot.py
# pages/2_🤖_Crop_Suggestion_Bot.py
import streamlit as st
# --- START: THEMING & EFFECTS BLOCK ---
# Initialize session state for theme and disco mode if they don't exist
if "theme" not in st.session_state:
 st.session_state.theme = "light"
if "disco_mode" not in st.session_state:
 st.session_state.disco_mode = False

# --- CSS DEFINITIONS ---

light_theme_css = """
<style>
 .stApp { background-color: #FFFFFF; color: #000000; }
 .stSidebar { background-color: #F0F2F6; }
</style>
"""

dark_theme_css = """
<style>
    /* Main app background and text */
 .stApp { background-color: #0E1117; color: #FFFFFF; }

    /* Sidebar styling with white text */
 .stSidebar { background-color: #1c1c1c; color: #FFFFFF; }

    /* Make headers and markdown text white */
 h1, h2, h3, h4, h5, h6, .stMarkdown { color: #FFFFFF; }

    /* Style for expanders */
 .stExpander { background-color: #1c1c1c; }

    /* Style for text areas */
 .stTextArea textarea { background-color: #262730; color: #FFFFFF; }

    /* Style for buttons */
 .stButton>button { color: #FFFFFF; background-color: #3498db; border-color: #3498db; }

    /* Ensure metric labels are visible */
 .stMetric_container .stMetricLabel { color: #a0a0a0; }
</style>
"""

disco_css = """
<style>
    @keyframes disco-text {
        0% { color: red; } 15% { color: orange; } 30% { color: yellow; }
        45% { color: green; } 60% { color: blue; } 75% { color: indigo; }
        90% { color: violet; } 100% { color: red; }
    }
    h1, h2, h3 { animation: disco-text 4s infinite; }
</style>

"""

# --- SIDEBAR BUTTONS ---

# A container to group the buttons with
with st.sidebar:
 st.write("---") # A small separator
 if st.button(f"Switch to {'Dark' if st.session_state.theme == 'light' else 'Light'} Mode", key="theme_toggle_bot"):
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

 if st.button("🕺 Toggle Disco Mode", key="disco_toggle_bot"):
    st.session_state.disco_mode = not st.session_state.disco_mode

# --- CSS INJECTION LOGIC ---

# Apply the selected theme's CSS
st.markdown(dark_theme_css if st.session_state.theme == "dark" else light_theme_css, unsafe_allow_html=True)

# Apply disco CSS if disco mode is active (this will override parts of the theme)
if st.session_state.disco_mode:
 st.session_state.theme = "disco" # Set theme to disco when disco mode is active
 st.markdown(disco_css, unsafe_allow_html=True)
# --- END: THEMING & EFFECTS BLOCK ---

st.title("🤖 AI Crop Suggestion Bot")
st.markdown("Get an intelligent crop recommendation based on your farm's conditions.")

# --- User Inputs for the Bot ---
col1, col2 = st.columns(2)

with col1:
    sowing_month = st.selectbox("Select Sowing Month", 
        ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    soil_type = st.selectbox("Select Soil Type", 
        ["Alluvial Soil", "Sandy Soil", "Clay Soil"])

with col2:
    water_availability = st.selectbox("Water Availability", 
        ["High (Canal + Tubewell)", "Medium (Canal or Tubewell)", "Low (Rain-fed)"])
    market_risk = st.selectbox("Your Market Risk Appetite", 
        ["Low (Prefer MSP Crops)", "Medium (Balanced)", "High (Cash Crops)"])

# --- The "AI" Logic (Rule-Based System) ---
def suggest_crop(month, water, soil, risk):
    # Rabi crops (Winter)
    if month in ["October", "November", "December"]:
        if water in ["High (Canal + Tubewell)", "Medium (Canal or Tubewell)"]:
            return "🌾 Wheat", "Ideal for Rabi season with good water supply. Strong MSP support."
        else:
            return "🌽 Maize", "Requires less water than wheat, suitable for rain-fed winter cultivation."
    
    # Kharif crops (Summer/Monsoon)
    elif month in ["June", "July", "August"]:
        if water == "High (Canal + Tubewell)":
            return "🍚 Rice (Paddy)", "Thrives in monsoon season with abundant water. Strong MSP support."
        elif water == "Medium (Canal or Tubewell)":
            if risk == "High (Cash Crops)":
                return "🌱 Cotton", "A cash crop that does well with moderate water in this season."
            else:
                return "🌽 Maize", "A versatile crop that requires less water than rice."
        else: # Low water
            return "🌾 Millets (Bajra)", "Highly drought-resistant and suitable for rain-fed conditions."
    
    # Zaid crops (Summer)
    elif month in ["March", "April", "May"]:
        return "🍉 Watermelon/Vegetables", "These cash crops grow quickly in the summer season with moderate irrigation."
        
    else:
        return "❓ No primary crop", "This is an off-season month for major crops in Punjab. Consider fodder or short-cycle vegetables."

# --- Display the Suggestion ---
if st.button("💡 Get Suggestion"):
    crop_name, reason = suggest_crop(sowing_month, water_availability, soil_type, market_risk)
    
    st.markdown("---")
    st.subheader("AI Recommendation:")
    
    if "No primary crop" in crop_name:
        st.warning(f"**{crop_name}**: {reason}")
    else:
        st.success(f"**Suggested Crop: {crop_name}**")
        st.info(f"**Reasoning:** {reason}")
