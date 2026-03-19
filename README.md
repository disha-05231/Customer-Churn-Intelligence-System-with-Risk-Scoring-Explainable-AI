# Customer Churn Intelligence System with Risk Scoring & Explainable AI

## 1. Project Overview

This project implements a complete end-to-end Machine Learning system to predict customer churn using real-world telecom data.

The primary goal was to design a churn intelligence pipeline that is:
- Explainable
- Leakage-free
- Business-actionable
- Reusable across similar datasets

The dataset consists of approximately **100,000 telecom customers** with **200+ behavioral features** across multiple months, including:
- Usage patterns
- Recharge behavior
- Revenue metrics
- Customer engagement indicators

---

## 2. Objective

The system was designed with the following objectives:

- Predict customer churn based on historical behavioral data  
- Segment customers into **High, Medium, and Low risk categories**  
- Identify key churn drivers using explainable AI techniques  
- Generate **deployment-ready outputs** for business/retention teams  
- Ensure model robustness by addressing real-world ML challenges  

---

## 3. Churn Definition

Churn was defined using domain-specific logic:

- Customers with **zero revenue in Month 9 (arpu_9 == 0)** were labeled as churned  

This transformation converted raw behavioral data into a **supervised learning problem**.

---

## 4. Exploratory Data Analysis (EDA)

Initial analysis revealed several important patterns:

- Significant **class imbalance (~9% churn rate)**  
- Clear **decline in revenue and usage before churn**  
- Strong influence of **tenure and recharge behavior**  
- Feature relationships analyzed using a **correlation matrix**, focusing on high-variance features  

EDA helped identify meaningful signals and reduce redundant features.

---

## 5. Feature Engineering and Preprocessing

Key preprocessing steps included:

- Removal of **Month-9 features** to eliminate **data leakage**  
- Selection of **numeric features only** for modeling  
- Handling missing values using **median imputation**  
- Use of **stratified train-test split** to preserve churn distribution  

### Critical Insight:
Initial model performance was unrealistically high, indicating **data leakage**.  
Feature importance analysis revealed that **future-dependent variables (Month-9)** were dominating predictions.

These features were removed to ensure:
- Realistic evaluation
- Generalizable model performance

---

## 6. Model Development

Two models were implemented:

### 1. Logistic Regression
- Used as a baseline model  
- Provided interpretability  

### 2. Random Forest (Final Model)
- Captures non-linear relationships  
- Better performance on complex patterns  
- Selected as the final production model  

---

## 7. Validation Strategy

To ensure reliable and robust performance:

- Data split into **80% training / 20% testing**  
- Applied **Stratified K-Fold Cross-Validation** on training data  
- Used **ROC-AUC as the primary evaluation metric**  

### Final Random Forest Performance:
- **ROC-AUC ≈ 0.92**  
- **Accuracy ≈ 90%**  
- **Churn Recall ≈ 73%**  

These results indicate:
- Strong generalization  
- Controlled overfitting  
- Reliable predictive performance  

---

## 8. Engineering Challenges Addressed

This project focused heavily on solving real-world ML issues:

### Data Leakage
- Detected via unrealistic performance  
- Resolved by removing future-dependent features  

### Overfitting
- Controlled using cross-validation and proper evaluation  

### Missing Values
- Handled using median imputation  

### Class Imbalance
- Managed using **balanced class weights**  

### Prediction Scope
- Extended from test-only predictions to **full dataset scoring**  

### Business Requirements
- Generated **actionable outputs** for real-world usage  

---

## 9. Risk Scoring System

Predicted churn probabilities were converted into business-friendly categories:

- **High Risk ≥ 0.70**  
- **Medium Risk ≥ 0.40**  
- **Low Risk < 0.40**  

This allows business teams to:
- Prioritize high-risk customers  
- Optimize retention strategies  
- Allocate resources efficiently  

---

## 10. Explainable AI

Explainability was ensured using:

- **Random Forest feature importance**

Key churn drivers identified:
- Revenue decline  
- Recharge amount  
- Usage behavior  

This ensures:
- Transparency  
- Trust in model predictions  
- Better business decision-making  

---

## 11. Deployment-Oriented Outputs

The system generates multiple business-ready outputs:

- `all_customers_churn_risk.csv`  
  → Full dataset predictions with churn probabilities  

- `high_medium_risk_customers.csv`  
  → Filtered actionable list for retention teams  

- Automated **insight summary**, including:
  - Risk distribution  
  - Key churn drivers  

---

## 12. Dynamic Pipeline Design

The pipeline was designed for reusability and scalability:

- Preprocessing applied only to feature matrices  
- Original dataset remains unchanged  
- New telecom datasets with similar schema can be processed  
- Models can be retrained for different domains  

### Design Principle:
> The pipeline is reusable, the model is retrainable  

---

## 13. Final System Capabilities

The completed system includes:

- End-to-end ML pipeline  
- Leakage-free modeling  
- Exploratory data analysis with correlation matrix  
- Logistic Regression baseline  
- Random Forest final model  
- Stratified K-Fold validation  
- Explainable feature importance  
- Full dataset scoring  
- Risk segmentation  
- Business-ready CSV outputs  
- Automated insight generation  

---

## 14. Tech Stack

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Tools:** VS Code, Anaconda  

---

## 15. Conclusion

This project demonstrates a complete machine learning lifecycle:

- From raw data preprocessing  
- To model development and validation  
- To deployment-ready outputs  

The focus was on:
- Engineering rigor  
- Real-world problem solving  
- Model reliability  
- Business usability  

This reflects practical ML system design rather than purely academic modeling.
