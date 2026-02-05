This project builds an end-to-end Customer Churn Intelligence System using real-world telecom data (~100K customers) to predict churn risk and support retention decisions. Churn was defined using business logic (zero revenue in Month 9), followed by exploratory analysis, feature engineering, and preprocessing (handling missing values, class imbalance, and numeric feature selection). A Logistic Regression baseline was developed, then a Random Forest model was trained to capture non-linear behavior patterns, achieving ROC-AUC ≈ 0.92 on leakage-free test data. Predictions were converted into actionable Low / Medium / High risk segments, and customer-level outputs were generated for operational use.

A key learning in this project was identifying and fixing data leakage when unrealistically perfect results appeared. By analyzing feature importance, future Month-9 variables were removed, ensuring realistic model performance. The final system scores the entire customer base, produces prioritized churn lists, highlights top churn drivers using feature importance (Explainable AI), and exports business-ready CSV files for retention teams. The project emphasizes not just modeling, but building a reusable, explainable, and deployment-ready ML pipeline with careful validation and real-world considerations.

OUTPUT:



Dataset loaded: (99999, 226)

Churn distribution:
  churn
0       90930
1       9069
Name: count, dtype: int64

Leakage features removed

Model trained

Classification Report:

              precision    recall  f1-score   support

           0       0.97      0.92      0.95     18186
           1       0.48      0.73      0.58      1814

    accuracy                           0.90     20000
   macro avg       0.73      0.83      0.76     20000
weighted avg       0.93      0.90      0.91     20000

ROC-AUC: 0.9175198800196572

<img width="798" height="607" alt="Screenshot 2026-02-05 110005" src="https://github.com/user-attachments/assets/609b866c-6fb6-4aef-86ee-b728038ffd39" />


Risk Distribution:
 churn_risk_level
Low Risk       82012
High Risk       9130
Medium Risk     8857
Name: count, dtype: int64

Actionable customers: 17987

CSV files saved in project folder

Top 10 Churn Drivers:
 arpu_8                0.086380
total_rech_amt_8      0.075446
total_og_mou_8        0.074885
total_ic_mou_8        0.072597
last_day_rch_amt_8    0.067240
max_rech_amt_8        0.065930
loc_og_mou_8          0.043350
loc_og_t2t_mou_8      0.034989
loc_og_t2m_mou_8      0.029929
loc_ic_mou_8          0.029482
dtype: float64

INSIGHTS SUMMARY:

Total customers: 99999
High Risk: 9130
Medium Risk: 8857
Low Risk: 82012

Top churn drivers:
arpu_8                0.086380
total_rech_amt_8      0.075446
total_og_mou_8        0.074885
total_ic_mou_8        0.072597
last_day_rch_amt_8    0.067240


Process finished with exit code 0
