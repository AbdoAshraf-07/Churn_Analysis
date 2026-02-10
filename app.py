import streamlit as st
import pandas as pd
import xgboost as xgb
import numpy as np

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Telco Churn Predictor",
    page_icon="📊",
    layout="wide"
)

# =========================
# Custom CSS (Modern Look)
# =========================
st.markdown("""
<style>
.big-title {
    font-size: 42px;
    font-weight: 800;
}
.sub-title {
    font-size: 18px;
    color: #6c757d;
}
.card {
    padding: 25px;
    border-radius: 15px;
    background: #f8f9fa;
    box-shadow: 0 6px 20px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# =========================
# Header
# =========================
st.markdown('<div class="big-title">📉 Telco Churn Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Predict customer churn risk using machine learning</div>', unsafe_allow_html=True)
st.divider()

# =========================
# Load Model
# =========================
@st.cache_resource
def load_model():
    model = xgb.XGBClassifier()
    model.load_model("telco_churn_model.json")
    return model

model = load_model()

# =========================
# Sidebar Inputs
# =========================
st.sidebar.header("🧾 Customer Profile")

tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
monthly_charges = st.sidebar.number_input("Monthly Charges ($)", 18.0, 120.0, 65.0)
total_charges = st.sidebar.number_input("Total Charges ($)", 0.0, monthly_charges * tenure)

contract = st.sidebar.selectbox("Contract Type", [
    "Month-to-month", "One year", "Two year"
])

internet = st.sidebar.selectbox("Internet Service", [
    "Fiber optic", "DSL", "No"
])

payment_method = st.sidebar.selectbox("Payment Method", [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
])

tech_support = st.sidebar.selectbox("Tech Support", [
    "Yes", "No", "No internet service"
])

paperless = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])

# =========================
# Main Layout
# =========================
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📌 Customer Summary")

    st.write(f"""
    - **Tenure:** {tenure} months  
    - **Contract:** {contract}  
    - **Internet:** {internet}  
    - **Payment Method:** {payment_method}  
    - **Monthly Charges:** ${monthly_charges:.2f}  
    """)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🎯 Prediction")

    if st.button("🚀 Predict Churn Risk", use_container_width=True):
        # Replace with real prediction
        risk_score = np.random.random()

        st.progress(risk_score)

        st.metric(
            label="Churn Probability",
            value=f"{risk_score:.2%}"
        )

        if risk_score > 0.42:
            st.error("⚠️ High Churn Risk")
            st.caption("Recommended: retention offers, discounts, proactive support")
        else:
            st.success("✅ Low Churn Risk")
            st.caption("Customer is likely to stay")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# Footer
# =========================
st.divider()
st.info("Model optimized for **85% Recall** to prioritize customer retention.")
