import streamlit as st
import json
import os
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="GenZ Mental Health Advice Engine", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for modern Advice Blocks
st.markdown("""
<style>
    .advice-header {
        font-size: 20px;
        font-weight: bold;
        color: #1E1B4B;
        margin-bottom: 10px;
    }
    .low-stress {
        background-color: #f0fdf4;
        padding: 20px;
        border-radius: 10px;
        border-left: 6px solid #16a34a;
        margin-bottom: 15px;
    }
    .med-stress {
        background-color: #fffbeb;
        padding: 20px;
        border-radius: 10px;
        border-left: 6px solid #d97706;
        margin-bottom: 15px;
    }
    .high-stress {
        background-color: #fef2f2;
        padding: 20px;
        border-radius: 10px;
        border-left: 6px solid #dc2626;
        margin-bottom: 15px;
    }
    .slang-chip {
        background-color: #e0e7ff;
        color: #4338ca;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 500;
        display: inline-block;
        margin-right: 5px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 Adaptive GenZ Stress Response & Advice Engine")
st.write("Input a customized stress level to evaluate matching conversational tactics and clinical guidance frameworks.")

# --- 1. DATASET SCHEMA FALLBACK ---
@st.cache_data
def load_metadata_safely():
    filename = "teen-mental-health-chatbot-dataset-metadata.json"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        # Graceful schema fallback so the application survives runtime standalone
        return {
            "alternateName": "Dataset for fine tuning mental health chatbot aimed at teenagers",
            "license": "MIT"
        }

metadata = load_metadata_safely()

# --- 2. SIDEBAR CONFIGURATION ---
st.sidebar.markdown("### 🛠️ System Reference")
st.sidebar.markdown(f"**Target Objective:**\n{metadata.get('alternateName')}")
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Dataset Balance Target")
st.sidebar.write("• **60%** Negative/Anxious Spectrum")
st.sidebar.write("• **40%** Positive/Neutral Spectrum")

# --- 3. HIGH LEVEL OVERVIEW ---
st.subheader("📌 Global Dataset Support Overview")
col_stat1, col_stat2, col_stat3 = st.columns(3)
with col_stat1:
    st.metric(label="Total Blueprint Lines", value="200 Dialogues")
with col_
