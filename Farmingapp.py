import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Smart Farming Assistant", layout="centered")

# Title
st.title("🌱 Smart Farming Assistant") how to run this program?

# Sample dataset
data = {
    "Soil": ["Sandy", "Clay", "Loamy", "Sandy", "Clay"],
    "Weather": ["Hot", "Rainy", "Moderate", "Moderate", "Hot"],
    "Crop": ["Millet", "Rice", "Wheat", "Groundnut", "Cotton"]
}

df = pd.DataFrame(data)

# Crop recommendation function
def recommend_crop(soil, weather):
    result = df[(df["Soil"] == soil) & (df["Weather"] == weather)]
    if not result.empty:
        return result["Crop"].values[0]
    else:
        return "Wheat (General Recommendation)"

# Farming tips
def get_tips(crop):
    tips = {
        "Rice": "💧 Requires plenty of water and irrigation.",
        "Wheat": "🌞 Needs moderate climate and sunlight.",
        "Millet": "🌵 Grows well in dry areas with less water.",
        "Cotton": "☀️ Requires warm climate and proper care.",
        "Groundnut": "🌿 Best in sandy soil with moderate rain."
    }
    return tips.get(crop, "🌱 Follow basic farming practices.")

# Input section
st.subheader("🔍 Enter Details")

soil = st.selectbox("Select Soil Type", ["Sandy", "Clay", "Loamy"])
weather = st.selectbox("Select Weather", ["Hot", "Rainy", "Moderate"])

# Button
if st.button("Get Recommendation"):
    crop = recommend_crop(soil, weather)

    st.subheader("🌾 Recommended Crop:")
    st.success(crop)

    st.subheader("📌 Farming Tips:")
    st.info(get_tips(crop))

# Footer
st.markdown("---")
st.markdown("👨‍💻 Built using Python & Streamlit")