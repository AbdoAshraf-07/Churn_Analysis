Telco Customer Churn Analysis
Overview

This project aims to predict customer churn for a telecommunications company. By identifying customers likely to leave, the business can take proactive retention actions and improve customer loyalty.

Roles

Machine Learning Engineer: Built predictive models using XGBoost, handled imbalanced data, feature engineering, and threshold tuning.

Data Analyst: Created a dynamic Power BI dashboard to visualize insights, track trends, and support data-driven decision-making.

Dataset

The dataset includes customer demographics, account information, and service details. A sample file used in this project:

WA_Fn-UseC_-Telco-Customer-Churn.csv

Key Steps

Data Preprocessing

Handling missing values

Encoding categorical variables

Scaling numerical features

Exploratory Data Analysis (EDA)

Understanding feature distributions

Identifying churn drivers

Model Development

XGBoost classifier

Handling class imbalance using scale_pos_weight

Threshold tuning for high recall

Dashboard Visualization

Interactive Power BI dashboard for insights and trend tracking

Results

Recall: 85%

Top churn drivers: Month-to-month contracts, Fiber Optic service

Enables identification of 4 out of 5 potential churners for targeted retention campaigns

Files Included

app.py – Main Python application (if applicable)

modeling.ipynb, preprocessing.ipynb, understanding.ipynb – Jupyter notebooks for EDA and model building

telco_churn_model.json – Saved ML model

telco-churn.pbix – Power BI dashboard file

DataModel, DiagramLayout, Metadata, Report – Power BI project folders

How to Run

Clone the repository:

git clone https://github.com/AbdoAshraf-07/Churn_Analysis.git


Install required Python packages:

pip install -r requirements.txt


Run app.py or open the notebooks for analysis.

Open telco-churn.pbix in Power BI to explore the dashboard.

Tools & Technologies

Python: Pandas, NumPy, XGBoost, scikit-learn

Power BI: Interactive dashboards

Jupyter Notebook: Data exploration and modeling

License

This project is for educational purpose
