import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset 
data_path = r"/content/telecom_churn_data.csv"
df = pd.read_csv(data_path)

print("Dataset loaded:", df.shape)


# Create churn label (month 9 revenue = 0 → churn)
df['churn'] = np.where(df['arpu_9'] == 0, 1, 0)
print("\nChurn distribution:\n", df['churn'].value_counts())


# Separate features and target
y = df['churn']
X = df.drop(columns=['churn'])

# Remove month-9 leakage features
X = X.drop(columns=[c for c in X.columns if c.endswith('_9')])
print("\nLeakage features removed")

# Keep numeric columns only and fill missing values
X = X.select_dtypes(include=['int64', 'float64'])
X = X.fillna(X.median())


# Train–test split for evaluation
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Random Forest model
rf_model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)
print("\nModel trained")


# Test set evaluation
y_pred = rf_model.predict(X_test)
y_prob = rf_model.predict_proba(X_test)[:, 1]

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

roc_auc = roc_auc_score(y_test, y_prob)
print("ROC-AUC:", roc_auc)


# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


#Score ALL customers

X_full = df.drop(columns=['churn'])
X_full = X_full.drop(columns=[c for c in X_full.columns if c.endswith('_9')])
X_full = X_full.select_dtypes(include=['int64', 'float64'])
X_full = X_full.fillna(X_full.median())

full_prob = rf_model.predict_proba(X_full)[:, 1]

final_output = pd.DataFrame({
    'customer_id': df['mobile_number'],
    'churn_probability': full_prob
})

# Risk buckets
def assign_risk(p):
    if p >= 0.70:
        return "High Risk"
    elif p >= 0.40:
        return "Medium Risk"
    else:
        return "Low Risk"

final_output['churn_risk_level'] = final_output['churn_probability'].apply(assign_risk)

print("\nRisk Distribution:\n", final_output['churn_risk_level'].value_counts())


# High + Medium risk customers
actionable_customers = final_output[
    final_output['churn_risk_level'].isin(['High Risk', 'Medium Risk'])
]

print("\nActionable customers:", actionable_customers.shape[0])


# Save CSV outputs
base_path = os.path.dirname(os.path.abspath(__file__))
final_output.to_csv(os.path.join(base_path, "all_customers_churn_risk.csv"), index=False)
actionable_customers.to_csv(os.path.join(base_path, "high_medium_risk_customers.csv"), index=False)

print("\nCSV files saved in project folder")


# Feature importance (Explainable AI)
feature_importance = pd.Series(rf_model.feature_importances_, index=X.columns).sort_values(ascending=False)

print("\nTop 10 Churn Drivers:\n", feature_importance.head(10))


# Automated insight summary (LLM-ready text)
summary_text = f"""
Total customers: {len(final_output)}
High Risk: {(final_output['churn_risk_level']=='High Risk').sum()}
Medium Risk: {(final_output['churn_risk_level']=='Medium Risk').sum()}
Low Risk: {(final_output['churn_risk_level']=='Low Risk').sum()}

Top churn drivers:
{feature_importance.head(5).to_string()}
"""

print("\nINSIGHTS SUMMARY:")
print(summary_text)
