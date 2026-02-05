<img width="798" height="607" alt="Screenshot 2026-02-05 110005" src="https://github.com/user-attachments/assets/0fb19f8f-e0e0-4833-9c3e-9ecf361d4b18" />This project builds an end-to-end Customer Churn Intelligence System using real-world telecom data (~100K customers) to predict churn risk and support retention decisions. Churn was defined using business logic (zero revenue in Month 9), followed by exploratory analysis, feature engineering, and preprocessing (handling missing values, class imbalance, and numeric feature selection). A Logistic Regression baseline was developed, then a Random Forest model was trained to capture non-linear behavior patterns, achieving ROC-AUC ≈ 0.92 on leakage-free test data. Predictions were converted into actionable Low / Medium / High risk segments, and customer-level outputs were generated for operational use.

A key learning in this project was identifying and fixing data leakage when unrealistically perfect results appeared. By analyzing feature importance, future Month-9 variables were removed, ensuring realistic model performance. The final system scores the entire customer base, produces prioritized churn lists, highlights top churn drivers using feature importance (Explainable AI), and exports business-ready CSV files for retention teams. The project emphasizes not just modeling, but building a reusable, explainable, and deployment-ready ML pipeline with careful validation and real-world considerations.

OUTPUT:
Dataset loaded successfully
Dataset shape: (99999, 226)

Churn distribution:
churn
0    90930
1     9069
Name: count, dtype: int64

Removed 54 leakage features

Train-test split completed
Model training completed

CLASSIFICATION REPORT (TEST DATA):

              precision    recall  f1-score   support

           0       0.97      0.92      0.95     18186
           1       0.48      0.73      0.58      1814

    accuracy                           0.90     20000
   macro avg       0.73      0.83      0.76     20000
weighted avg       0.93      0.90      0.91     20000

ROC-AUC Score: 0.9175198800196572
<img width="797" height="597" alt="image" src="https://github.com/user-attachments/assets/f75dad9a-5943-4aca-9503-f703335565f8" /<img width="798" height="607" alt="Screenshot 2026-02-05 110005" src="https://github.com/user-attachments/assets/8eda3ae0-8b98-4703-8500-3ec151a65cf3" />

