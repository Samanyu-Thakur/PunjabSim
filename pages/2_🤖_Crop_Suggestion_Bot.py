# pages/2_🤖_Crop_Suggestion_Bot.py
import streamlit as st

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