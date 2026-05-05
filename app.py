import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time

# Page configuration
st.set_page_config(
    page_title="LoanRisk AI - Smart Loan Approval System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .main-header {
        animation: fadeInUp 0.8s ease-out;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
    }
    .sub-header {
        animation: slideInLeft 0.6s ease-out;
        text-align: center;
        color: #666;
        margin-bottom: 30px;
    }
    .feature-card {
        animation: fadeInUp 0.5s ease-out;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        transition: transform 0.3s;
    }
    .feature-card:hover { transform: translateY(-10px); }
    .approved {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        text-align: center;
        padding: 20px;
        border-radius: 15px;
        animation: pulse 0.5s ease-out;
    }
    .rejected {
        background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
        color: white;
        text-align: center;
        padding: 20px;
        border-radius: 15px;
        animation: pulse 0.5s ease-out;
    }
    .risk-low {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    .risk-medium {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    .risk-high {
        background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 10px 30px;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 25px;
        transition: all 0.3s;
        width: 100%;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
    }
    .progress-text {
        text-align: center;
        color: #667eea;
        font-size: 1.2rem;
        margin-top: 20px;
    }
    div.stNumberInput > div > input { border-radius: 10px; }
    div.stSelectbox > div > select { border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# Load models with caching
@st.cache_resource
def load_models():
    with st.spinner("🚀 Loading AI Models..."):
        time.sleep(1)
        model1 = joblib.load('final_model1.pkl')
        model2 = joblib.load('final_model2.pkl')
        scaler = joblib.load('scaler.pkl')
        return model1, model2, scaler

# Header Section
st.markdown('<div class="main-header">🏦 LoanRisk AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Intelligent Loan Approval & Risk Assessment System</div>', unsafe_allow_html=True)

# Features Section
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>⚡</h3>
        <h4>Real-time Analysis</h4>
        <p>Instant loan approval decisions</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🎯</h3>
        <h4>90% Accuracy</h4>
        <p>Advanced ML algorithms</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🛡️</h3>
        <h4>Risk Assessment</h4>
        <p>Low/Medium/High risk levels</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="feature-card">
        <h3>🤖</h3>
        <h4>AI Powered</h4>
        <p>Smart decision making</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Load models
try:
    model1, model2, scaler = load_models()
    st.success("✅ AI Models Loaded Successfully!")
except Exception as e:
    st.error(f"❌ Error loading models: {str(e)}")
    st.stop()

# Main Form
st.markdown("## 📝 Loan Application Form")
st.markdown("*Fill in the details below for instant assessment*")

left_col, right_col = st.columns(2)

with left_col:
    with st.container():
        st.markdown("### 👤 Personal Information")
        gender = st.selectbox("Gender", ["Male", "Female"], key="gender")
        married = st.selectbox("Marital Status", ["Yes", "No"], key="married")
        dependents = st.selectbox("Number of Dependents", [0, 1, 2, 3], 
                                   format_func=lambda x: "3+" if x == 3 else str(x), key="dependents")
        education = st.selectbox("Education Level", ["Graduate", "Not Graduate"], key="education")
        self_employed = st.selectbox("Employment Type", ["No", "Yes"], key="self_employed")

with right_col:
    with st.container():
        st.markdown("### 💰 Financial Information")
        applicant_income = st.number_input("Applicant Income (₹)", min_value=0, value=5000, step=1000, key="app_income")
        coapplicant_income = st.number_input("Co-applicant Income (₹)", min_value=0, value=0, step=500, key="co_income")
        loan_amount = st.number_input("Loan Amount (₹)", min_value=0, value=150000, step=10000, key="loan_amt")
        loan_term = st.selectbox("Loan Term (days)", [360, 180, 120, 60], key="loan_term")
        credit_history = st.selectbox("Credit History", [1.0, 0.0], 
                                       format_func=lambda x: "Good (1.0)" if x == 1.0 else "Bad (0.0)", key="credit")
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"], key="property")

# Predict button
if st.button("🔍 ANALYZE APPLICATION", key="analyze_btn", use_container_width=True):
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    status_text.markdown('<p class="progress-text">📊 Processing application data...</p>', unsafe_allow_html=True)
    progress_bar.progress(25)
    time.sleep(0.5)
    
    # Prepare input data - dependents is already numeric!
    input_data = pd.DataFrame({
        'Gender': [1 if gender == "Male" else 0],
        'Married': [1 if married == "Yes" else 0],
        'Dependents': [dependents],
        'Education': [0 if education == "Graduate" else 1],
        'Self_Employed': [1 if self_employed == "Yes" else 0],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_term],
        'Credit_History': [credit_history],
        'Property_Area_Semiurban': [1 if property_area == "Semiurban" else 0],
        'Property_Area_Urban': [1 if property_area == "Urban" else 0]
    })
    
    status_text.markdown('<p class="progress-text">⚙️ Normalizing financial metrics...</p>', unsafe_allow_html=True)
    progress_bar.progress(50)
    time.sleep(0.5)
    
    numerical_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']
    input_data[numerical_cols] = scaler.transform(input_data[numerical_cols])
    
    status_text.markdown('<p class="progress-text">🧠 AI analyzing application...</p>', unsafe_allow_html=True)
    progress_bar.progress(75)
    time.sleep(0.5)
    
    # Make predictions with custom threshold
    approval_prob = model1.predict_proba(input_data)[0]
    threshold = 0.65  # Stricter threshold for approval
    
    if approval_prob[1] >= threshold:
        approval_pred = 1
    else:
        approval_pred = 0
    
    # Calculate risk score for approved loans
    if approval_pred == 1:
        risk_score = 0
        
        # Credit History (Biggest factor - 50 points)
        if credit_history == 0.0:
            risk_score += 50
        
        # Loan Amount (25 points)
        if loan_amount > 200000:
            risk_score += 25
        elif loan_amount > 150000:
            risk_score += 15
        elif loan_amount > 100000:
            risk_score += 5
        
        # Income to Loan Ratio (20 points)
        total_income = applicant_income + coapplicant_income
        if loan_amount > 0:
            income_ratio = total_income / loan_amount
            if income_ratio < 2:
                risk_score += 20
            elif income_ratio < 3:
                risk_score += 10
        
        # Dependents (15 points)
        if dependents == 3:
            risk_score += 15
        elif dependents == 2:
            risk_score += 10
        elif dependents == 1:
            risk_score += 5
        
        # Self Employed (10 points)
        if self_employed == "Yes":
            risk_score += 10
        
        # Determine Risk Level
        if risk_score >= 50:
            risk = "High"
            risk_icon = "🔴"
            risk_class = "risk-high"
        elif risk_score >= 30:
            risk = "Medium"
            risk_icon = "⚠️"
            risk_class = "risk-medium"
        else:
            risk = "Low"
            risk_icon = "✅"
            risk_class = "risk-low"
    else:
        risk = "High"
        risk_icon = "🔴"
        risk_class = "risk-high"
        risk_score = 100
    
    progress_bar.progress(100)
    status_text.markdown('<p class="progress-text">✅ Analysis complete!</p>', unsafe_allow_html=True)
    time.sleep(0.5)
    progress_bar.empty()
    status_text.empty()
    
    # Display Results
    st.markdown("---")
    st.markdown("## 📊 Assessment Results")
    
    result_col1, result_col2, result_col3 = st.columns(3)
    
    with result_col1:
        if approval_pred == 1:
            st.markdown("""
            <div class="approved">
                <h2>✅ APPROVED</h2>
                <p>Loan application has been approved</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="rejected">
                <h2>❌ REJECTED</h2>
                <p>Loan application has been declined</p>
            </div>
            """, unsafe_allow_html=True)
    
    with result_col2:
        st.markdown(f"""
        <div class="{risk_class}">
            <h2>{risk_icon} {risk} RISK</h2>
            <p>Risk level assessment</p>
        </div>
        """, unsafe_allow_html=True)
    
    with result_col3:
        confidence = approval_prob[1] if approval_pred == 1 else approval_prob[0]
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-align: center; padding: 20px; border-radius: 15px;">
            <h2>📈 {confidence*100:.1f}%</h2>
            <p>Confidence Score</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Detailed Analysis
    with st.expander("🔍 View Detailed Analysis", expanded=True):
        st.markdown("### Risk Factors Analyzed")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.metric("Credit History", "Good" if credit_history == 1.0 else "Poor")
            if loan_amount > 0:
                income_ratio = (applicant_income + coapplicant_income) / loan_amount * 100
                st.metric("Income to Loan Ratio", f"{income_ratio:.1f}%")
            
        with col_b:
            dependents_text = "3+" if dependents == 3 else str(dependents)
            impact = "High" if dependents == 3 else "Medium" if dependents in [1,2] else "Low"
            st.metric("Dependents", f"{dependents_text} ({impact} Impact)")
            st.metric("Employment Type", "Self Employed" if self_employed == "Yes" else "Salaried")
        
        st.markdown("### 💡 Recommendation")
        if approval_pred == 1:
            if risk == "Medium":
                st.info("⚠️ **Recommendation:** Loan approved with slightly higher interest rate due to medium risk profile.")
            else:
                st.success("✅ **Recommendation:** Loan approved with standard terms. Low risk profile detected.")
        else:
            st.error("❌ **Recommendation:** Loan rejected. Consider addressing credit history and reducing loan amount.")
    
    # Show balloons automatically if approved
    if approval_pred == 1:
        st.balloons()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>🏦 LoanRisk AI - Smart Loan Approval System</p>
    <p>Powered by Machine Learning | Real-time Risk Assessment | 24/7 Available</p>
    <small>© 2024 LoanRisk AI. All rights reserved.</small>
</div>
""", unsafe_allow_html=True)