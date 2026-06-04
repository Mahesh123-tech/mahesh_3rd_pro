import streamlit as st
import pandas as pd
import json
import os
import plotly.graph_objects as go

st.set_page_config(page_title="GenZ Chatbot Profile & Strategy Engine", layout="wide")

st.title("📊 Chatbot Dataset Fine-Tuning & Prompt Strategy Engine")
st.write("Enter your profile metrics and diagnostic attributes below to see how your simulated query matches up against dataset baselines and advice tiers.")

# 1. Load your baseline dataset safely
@st.cache_data
def load_data():
    filename = "teen-mental-health-chatbot-dataset-metadata.json"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        # Graceful schema fallback to ensure app compiles
        return {
            "alternateName": "Dataset for fine tuning mental health chatbot aimed at teenagers",
            "license": "MIT"
        }

metadata = load_data()

# Define structural mental health categories evaluated in the dataset
categories = [
    'Anxiety & Stress', 'Sadness & Depression', 'Insecurity & Self-Image', 
    'Peer Relationships & Loneliness', 'Academic & Finals Pressure', 'Daily Fatigue', 
    'Hope & Future Outlook', 'Resilience Training', 'Peer Support Networks', 
    'Grounding Exercises', 'Clinical Distress Markers', 'General Conversational'
]

# 2. Setup the User Input Form with a Submit Button
with st.form("user_budget_form"):
    st.subheader("📋 Step 1: Your Session Profile & Diagnostic Scores")
    
    # Form layout columns (Preserved original 3-column structural placement)
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1:
        user_name = st.text_input("User/Profile Name:", value="Alex")
    with col_p2:
        user_age = st.number_input("Target User Age Filter:", min_value=13, max_value=19, value=16)
    with col_p3:
        user_income = st.number_input("Total Manual Evaluation Stress Score (1-10 Scale):", min_value=1, max_value=10, value=7)
        
    st.markdown("---")
    st.markdown("##### Enter your estimated emotional trigger scores (0 to 100 max weight):")
    
    # Split the categories into two side-by-side columns for a clean look
    col_c1, col_c2 = st.columns(2)
    user_values = {}
    
    for i, cat in enumerate(categories):
        # Even indexes go to column 1, odd to column 2
        with col_c1 if i % 2 == 0 else col_c2:
            # Setting placeholder starting weights based on the 60/40 negative-to-positive dataset split
            if "Anxiety" in cat or "Sadness" in cat or "Insecurity" in cat or "Pressure" in cat:
                default_val = 65
            elif "Hope" in cat or "Resilience" in cat:
                default_val = 40
            else:
                default_val = 25
            user_values[cat] = st.number_input(f"{cat} Weight", min_value=0, max_value=100, value=default_val)
            
    # Form Submission button
    submit_button = st.form_submit_button(label="Analyze & Calculate Percentages")

# 3. Process data ONLY after the form is submitted
if submit_button:
    st.markdown("---")
    st.subheader(f"👋 Results and Strategy for {user_name} (Age {user_age})")
    
    # Mathematical total weight calculation
    total_allocated = sum(user_values.values())
    allocation_percentage = (total_allocated / 500) * 100 # Scaled against standard composite baseline max
    
    # Check stress triage alert tiers using your custom slider input variable (user_income)
    if user_income >= 8:
        st.error(f"🚨 **Critical Distress Notice:** Assigned Stress Level ({user_income}/10) requires immediate escalation framework routing to crisis channels: **1-800-273-8255**.")
    elif 4 <= user_income <= 7:
        st.warning(f"⚠️ **Moderate Distress Validation:** Assigned Stress Level ({user_income}/10) matches the dataset's **60% negative emotional buffer**. Employ empathetic mirroring: *'That really sucks to feel that way. Wanna talk about what's got you down?'*")
    else:
        st.success(f"✅ **Balanced Resiliency Zone:** Assigned Stress Level ({user_income}/10) maps within the **40% neutral/positive spectrum**. Apply validation techniques to sustain growth.")

    # KPI Summary Cards (Structured exactly like your original request)
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Evaluated Stress Score", f"{user_income} / 10")
    kpi2.metric("Total Cumulative Input Weights", f"{total_allocated} Units")
    kpi3.metric("Composite Density Index (%)", f"{allocation_percentage:.1f}%")

    # 4. Process Target Blueprint Benchmark Baselines (from JSON properties metadata)
    # 60% of focus targeting Negative Emotional spectrum topics vs 40% targeting Neutral/Positive Resilience
    peer_averages = [60.0 if i < 6 else 40.0 for i in range(len(categories))]
    user_list_values = [user_values[cat] for cat in categories]

    # 5. Plotly Grouped Bar Chart Setup (With original barmode bug fix retained)
    fig_comp = go.Figure()

    # User input weight trace
    fig_comp.add_trace(go.Bar(
        x=categories,
        y=user_list_values,
        name=f"{user_name}'s Selected Profile Matrix",
        marker_color='#4F46E5'
    ))

    # Target baseline benchmark trace
    fig_comp.add_trace(go.Bar(
        x=categories,
        y=peer_averages,
        name="Target Balanced Dataset Training Baseline",
        marker_color='#9CA3AF'
    ))

    fig_comp.update_layout(
        barmode='group',  
        title={
            'text': "Your Prompt Parameter Composition vs. Chatbot Training Baseline Target",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title="Diagnostic & Emotional Classification Sectors",
        yaxis_title="Attribute Weight / Density Intensity",
        legend_title="Comparison Matrices",
        template="plotly_white",
        height=550,
        margin=dict(t=80, b=40)
    )

    # Render layout in dashboard
    st.plotly_chart(fig_comp, use_container_width=True)

    # 6. Structured Breakdown Grid displaying calculations for every individual item
    st.markdown("### Detailed Itemized Breakdown & Alignment Strategies")
    
    breakdown_data = []
    for idx, cat in enumerate(categories):
        item_user_val = user_values[cat]
        item_peer_val = peer_averages[idx]
        item_percentage = (item_user_val / (total_allocated if total_allocated > 0 else 1)) * 100
        
        breakdown_data.append({
            "Category Area": cat,
            "Your Score Density": f"{item_user_val} Units",
            "Share of Total Diagnostic Portfolio (%)": f"{item_percentage:.1f}%",
            "Target Ideal Baseline Split": f"{item_peer_val}%"
        })
        
    st.table(pd.DataFrame(breakdown_data))
else:
    st.info("💡 Fill out the form fields above and click **'Analyze & Calculate Percentages'** to generate your operational diagnostic response reports.")
