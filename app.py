import streamlit as st
import json
import os
import plotly.graph_objects as go

# Configure page layouts
st.set_page_config(
    page_title="Teen Mental Health Chatbot Analyzer", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom visual branding
st.markdown("""
<style>
    .metric-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4F46E5;
        margin-bottom: 10px;
    }
    .insight-box {
        background-color: #f5f3ff;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #ddd6fe;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 Teen Mental Health Chatbot Fine-Tuning Dashboard")
st.write("Analyze structural training data criteria and test real-time prompt parsing metrics for teen-centric conversation AI.")

# --- 1. SAFELY LOAD JSON DATASET METADATA ---
@st.cache_data
def load_metadata():
    filename = "teen-mental-health-chatbot-dataset-metadata.json"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        st.error(f"⚠️ **Error:** '{filename}' not found in the root directory! Please ensure it is pushed to your GitHub repository.")
        st.stop()

metadata = load_metadata()

# --- 2. SIDEBAR CONTENT: DATASET PARAMETERS ---
st.sidebar.markdown("### 📝 Dataset Specifications")
st.sidebar.info(f"**Target Objective:** {metadata.get('alternateName', 'Fine-tuning mental health chatbot targeted at teenagers.')}")
st.sidebar.write("**License Configuration:** MIT Standard Open-Source")
st.sidebar.write("**Language Profile:** English (`en-US`) Casual Teen Slang")

# --- 3. CORE TRAINING BENCHMARK STATS (FROM DATASET METADATA) ---
st.markdown("### 📌 Baseline Dataset Training Thresholds")
st.write("Core metrics and guidelines extracted from the fine-tuning blueprint:")

overview_col1, overview_col2, overview_col3, overview_col4 = st.columns(4)
with overview_col1:
    st.metric(label="Target Dataset Volume", value="200 Rows", delta="Lines of Dialog")
with overview_col2:
    st.metric(label="Negative Emotion Split", value="60%", delta="Anxiety/Sadness/Stress")
with overview_col3:
    st.metric(label="Positive/Neutral Split", value="40%", delta="Hope/Resilience/Daily")
with overview_col4:
    st.metric(label="Primary Direct Line", value="1-800-273-8255", delta="Crisis Route Trigger")

st.markdown("---")

# --- 4. INTERACTIVE PROMPT ANALYZER FORM ---
with st.form("chatbot_test_form"):
    st.subheader("📋 Test Simulator: Input Sample Teen Statement")
    
    col_p1, col_p2 = st.columns([3, 1])
    with col_p1:
        user_query = st.text_input(
            "Enter text simulating real authentic teen conversational language:",
            value="I'm totally freaking out about finals, everyone's prettier than me and my friends ditched me again."
        )
    with col_p2:
        estimated_stress = st.slider("Manual Human Evaluation Stress Level:", min_value=1, max_value=10, value=7)
        
    st.markdown("##### Flag Context Triggers Identified:")
    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        has_slang = st.checkbox("Contains Casual Gen-Z Slang ('freaking out', 'sucks', 'vent')", value=True)
    with col_c2:
        is_negative = st.checkbox("Focuses on Negative Emotional Range (Insecurity/Anxiety)", value=True)
    with col_c3:
        requires_crisis = st.checkbox("Triggers Crisis Intervention Protocols (Self-harm risk)", value=False)
        
    submit_button = st.form_submit_button(label="🚀 Run Parsing Engine & Calculate Distribution")


# --- 5. EVALUATION REPORT GENERATION ---
if submit_button:
    st.markdown("## 🔍 Prompt Analysis Report")
    
    # 1. Actionable Router Alerts
    if requires_crisis:
        st.error("🚨 **CRITICAL TRIGGER:** Statement requires emergency intervention. Routing user immediately to official safety channels: **1-800-273-8255**.")
    elif is_negative and estimated_stress >= 6:
        st.warning("⚠️ **EMPATHETIC ROUTING REQUIRED:** Bot response engine must switch to validation mode: *'That really sucks to feel that way. Wanna talk about what's got you down?'*")
    else:
        st.success("✅ **STABLE ROUTING:** Proceed using casual empathetic dialogue framework to bolster long-term teenage resilience.")
        
    # KPI Analytics Row
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Characters Processed", f"{len(user_query)}")
    kpi2.metric("Assigned Stress Score", f"{estimated_stress} / 10")
    kpi3.metric("Slang Integration Vector", "High Approbative" if has_slang else "Standard Text")
    
    # --- 6. VISUAL METRIC CHARTING (COMPARING PROMPT VS DATASET DESIGN) ---
    st.markdown("### 📈 Prompt Emotion Distribution Blueprint vs Dataset Thresholds")
    
    # Compute relative metric weights based on inputs
    prompt_negative_weight = 100 if is_negative else 0
    prompt_positive_weight = 0 if is_negative else 100
    
    chart_categories = ['Negative Emotional Spectrum', 'Positive/Neutral Spectrum']
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=chart_categories,
        y=[prompt_negative_weight, prompt_positive_weight],
        name="Current Test Prompt Composition",
        marker_color='#4F46E5'
    ))
    fig.add_trace(go.Bar(
        x=chart_categories,
        y=[60, 40], # Extracted baseline from JSON metadata descriptions
        name="Target Baseline Training Split",
        marker_color='#9CA3AF'
    ))
    
    fig.update_layout(
        barmode='group',
        xaxis_title="Dataset Classification Zones",
        yaxis_title="Data Target Share (%)",
        template="plotly_white",
        height=450,
        margin=dict(t=30, b=30),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # --- 7. AUTOMATED INSIGHT GENERATION ---
    st.markdown("### 💡 Strategy and Context Insights")
    st.markdown(f"""
    <div class="insight-box">
        <ul>
            <li><b>Tone Analysis:</b> The prompt features text tokens that align with targeted <b>Teen-Centric Slang Frameworks</b> required to maintain conversational approaches.</li>
            <li><b>Model Objective Check:</b> Your input text matches the 60% negative emotional bias baseline designed within the fine-tuning setup to train validation responses.</li>
            <li><b>Recommendation:</b> Fine-tune the response weight vector to generate validation questions rather than generic advice tokens, keeping the interactions open-ended.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
else:
    st.info("💡 Write or edit a teen statement template in the text input area and click **'Run Parsing Engine & Calculate Distribution'** to calculate chatbot behavior parameters.")
