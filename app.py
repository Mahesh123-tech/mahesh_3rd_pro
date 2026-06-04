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
            "alternateName": "Dataset for fine tuning mental health chatbot aimed at teenagers[cite: 1]",
            "license": "MIT"
        }

metadata = load_metadata_safely()

# --- 2. SIDEBAR CONFIGURATION ---
st.sidebar.markdown("### 🛠️ System Reference")
st.sidebar.markdown(f"**Target Objective:**\n{metadata.get('alternateName')}")
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Dataset Balance Target")
st.sidebar.write("• **60%** Negative/Anxious Spectrum[cite: 1]")
st.sidebar.write("• **40%** Positive/Neutral Spectrum[cite: 1]")

# --- 3. HIGH LEVEL OVERVIEW ---
st.subheader("📌 Global Dataset Support Overview")
col_stat1, col_stat2, col_stat3 = st.columns(3)
with col_stat1:
    st.metric(label="Total Blueprint Lines", value="200 Dialogues")
with col_stat2:
    st.metric(label="Target Demographic", value="Teenagers / Gen-Z[cite: 1]")
with col_stat3:
    st.metric(label="Emergency Response Line", value="1-800-273-8255[cite: 1]")

st.markdown("---")

# --- 4. INTERACTIVE STRESS CONTROL CENTER ---
st.markdown("### 📋 Step 1: Adjust Stress Metrics")
with st.form("advice_generator_form"):
    
    # Large responsive slider
    user_stress = st.slider(
        "Select Current Stress Level Baseline:", 
        min_value=1, 
        max_value=10, 
        value=5,
        help="1-3: Low/Manageable | 4-7: Moderate/Validation Needed | 8-10: High/Action Required"
    )
    
    # FIXED: Split layout creation and block instantiation correctly here
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        primary_worry = st.selectbox(
            "Primary Stress Core Subject:",
            ["Academic / Finals Pressure", "Social Isolation & Peer Relationships", "Self-Image & Comparison Insecurities", "General Daily Fatigue"]
        )
    with col_input2:
        use_slang_responses = st.checkbox("Mirror Relatable Teen Tone/Slang phrases", value=True)
        
    submit_btn = st.form_submit_button(label="🎯 Generate Targeted Advice & Strategy")


# --- 5. ADAPTIVE ADVICE & SIMULATION OUTPUT ---
if submit_btn:
    st.markdown("---")
    st.markdown(f"## ⚡ Strategy Engine Output for Stress Level {user_stress}/10")
    
    # Categorize Advice Tiers
    if user_stress <= 3:
        # LOW STRESS TIER
        st.markdown(f"""
        <div class="low-stress">
            <div class="advice-header">🟢 Tier 1 Strategy: Reinforce Positive/Neutral Resilience</div>
            <p>Your current level falls within the dataset's <b>40% positive/neutral buffer zone</b>[cite: 1]. Focus is placed on positive validation and emotional grounding strategies.</p>
            <ul>
                <li><b>Actionable Advice:</b> Remind yourself of small positive events. Did you get a good grade or share a laugh with a friend today? Document it[cite: 1].</li>
                <li><b>Mental Exercise:</b> Grounding exercise. Step back from the workload for 15 minutes to reset your cognitive baselines.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif 4 <= user_stress <= 7:
        # MODERATE STRESS TIER
        st.markdown(f"""
        <div class="med-stress">
            <div class="advice-header">🟡 Tier 2 Strategy: Active Validation & Supportive Venting</div>
            <p>Your situation maps into the core <b>60% negative emotional range</b> of the training dataset[cite: 1]. Active validation is prioritized over direct problem-solving.</p>
            <ul>
                <li><b>Actionable Advice:</b> It is completely valid to feel overwhelmed by <b>{primary_worry}</b> right now[cite: 1]. Do not force immediate toxic positivity; allow space to vent[cite: 1].</li>
                <li><b>Mental Exercise:</b> Brain-dump journal. Spend 5 minutes writing down every single item causing cognitive friction, then visually separate what you can control from what you cannot.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        # HIGH STRESS TIER
        st.markdown(f"""
        <div class="high-stress">
            <div class="advice-header">🔴 Tier 3 Strategy: Escalation Protocol & Crisis De-escalation</div>
            <p>Critical distress marker detected. Automated safety systems must bypass casual dialogue scripts and switch to explicit protective guidance.</p>
            <ul>
                <li><b>Actionable Advice:</b> High-intensity stress spikes regarding <b>{primary_worry}</b> require human-in-the-loop support networks. Reach out to trusted peers, family, or counselors.</li>
                <li><b>Emergency Resource:</b> If thoughts turn toward self-harm or feel completely unmanageable, connect with the structured support line immediately at <b>1-800-273-8255</b>[cite: 1].</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Tone Profile Summary Visual Blocks
    st.markdown("### 💬 Conversational Tone Adjustment Matrix")
    if use_slang_responses:
        st.markdown("""
        <span class="slang-chip">"freaking out" mirroring allowed</span>
        <span class="slang-chip">"vent" context triggers on</span>
        <span class="slang-chip">"spill the tea" casual phrasing active</span>
        """, unsafe_allow_html=True)
        st.caption("Approachable, peer-level framing is turned on to make the support advice feel organic[cite: 1].")
    else:
        # FIXED: Resolved outer vs inner single-quote crash here
        st.markdown('<span class="slang-chip">Standard Professional English Mode</span>', unsafe_allow_html=True)
        st.caption("Standard clinical validation layout selected.")

    # --- 6. INTERACTIVE GAUGES & CHARTS ---
    st.markdown("---")
    st.markdown("### 📊 Dataset Alignment Visualizer")
    
    # Generate dynamic Plotly Gauge chart
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = user_stress,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Current Score Target Range", 'font': {'size': 20}},
        gauge = {
            'axis': {'range': [None, 10], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#4338ca"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [1, 3.9], 'color': '#f0fdf4'},
                {'range': [4, 7.9], 'color': '#fffbeb'},
                {'range': [8, 10], 'color': '#fef2f2'}
            ],
        }
    ))
    
    fig.update_layout(height=350, margin=dict(t=30, b=10))
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("💡 Adjust the slider controls above and press **'Generate Targeted Advice & Strategy'** to simulate the safety and advice protocols.")
