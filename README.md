🔮 Telco Customer Churn Prediction & Analytics
This project provides an end-to-end solution for predicting customer churn in the telecommunications industry. By leveraging XGBoost and Streamlit, we've built a tool that identifies at-risk customers with high sensitivity, allowing for proactive retention strategies.

🚀 Key Features
High Sensitivity Model: Optimized for 81% Recall to ensure that 4 out of 5 potential churners are identified.

Interactive Streamlit UI: A user-friendly interface for real-time churn risk assessment.

Integrated BI Dashboard: A built-in Power BI tab for deep-diving into historical trends and churn drivers.

Feature Importance Insights: Transparent decision-making by highlighting the primary factors driving churn.

🛠️ Technical Stack
Language: Python

Machine Learning: XGBoost Classifier

Data Manipulation: Pandas, NumPy

Web Framework: Streamlit

Business Intelligence: Power BI (Embedded)

Model Management: Joblib / JSON serialization

📊 Business Insights
Our analysis revealed that the top drivers for customer churn are:

Contract Type: Month-to-month contracts are the highest risk factor.

Internet Service: Fiber Optic users show a higher tendency to leave compared to DSL users.

Payment Method: Electronic check users are more likely to churn than those on automated payment plans.

⚙️ How to Run
Clone the repository:


git clone https://github.com/YourUsername/Telco-Churn-Prediction.git
Install dependencies:

pip install -r requirements.txt
Run the App:

streamlit run app.py
👥 Contributors
Developed by:

Abdelrahman Farag Mohamed - Generative AI Specialist

Hanaa Alaa - Dara Analyst

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
