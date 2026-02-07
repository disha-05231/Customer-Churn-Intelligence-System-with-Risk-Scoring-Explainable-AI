Project Overview

This project implements an end-to-end Machine Learning system to predict customer churn using real-world telecom data. The goal was to build a complete churn intelligence pipeline that is explainable, leakage-free, business-actionable, and reusable across similar datasets.

The dataset contains approximately 100,000 telecom customers with over 200 behavioral features across multiple months, including usage, recharge, revenue, and engagement metrics.

Objective

The system was designed to:

Predict customer churn based on historical behavior

Segment customers into High, Medium, and Low risk groups

Identify key churn drivers using explainable AI

Generate deployable CSV outputs for retention teams

Validate model stability and address practical ML challenges such as data leakage and class imbalance

Churn Definition

Churn was defined using domain logic:

Customers with zero revenue (arpu_9 == 0) in Month 9 were labeled as churned.

This transformed raw behavioral data into a supervised learning problem.

Exploratory Data Analysis

Initial analysis revealed:

Significant class imbalance (~9% churn)

Revenue and usage decline as primary churn indicators

Strong influence of tenure and recharge behavior

A correlation matrix (top high-variance features) was generated to understand feature relationships and detect redundancy.

Feature Engineering and Preprocessing

Key preprocessing steps included:

Removal of Month-9 features to eliminate data leakage

Selection of numeric features only

Median imputation for missing values

Stratified train-test split to preserve churn distribution

A critical learning point was identifying data leakage through unrealistically high initial performance. Feature importance analysis revealed future Month-9 variables dominating predictions. These were removed to restore realistic evaluation.

Model Development

Two models were implemented:

Logistic Regression (baseline)

Random Forest (primary model)

Random Forest was selected as the final model due to its ability to capture non-linear behavior patterns and its superior ROC-AUC performance.

Validation Strategy

To ensure reliable performance:

Holdout test set (80/20 split) was used

Stratified K-Fold cross-validation was applied on training data to validate model stability

ROC-AUC was chosen as the primary evaluation metric

Final Random Forest performance:

ROC-AUC ≈ 0.92

Accuracy ≈ 90%

Churn recall ≈ 73%

These results confirmed good generalization without overfitting.

Engineering Challenges Addressed

Several real-world ML issues were identified and resolved:

Data Leakage: Detected via unrealistically high performance and corrected by removing Month-9 features

Overfitting Concerns: Mitigated using cross-validation and test-set evaluation

Missing Values: Handled using median imputation

Class Imbalance: Managed using balanced class weights

Test vs Full Dataset Predictions: Extended from test-only predictions to scoring the full customer base

Business Output Requirements: Added CSV exports for operational use

Risk Scoring System

Predicted churn probabilities were converted into business-friendly risk tiers:

High Risk ≥ 0.70

Medium Risk ≥ 0.40

Low Risk < 0.40

This enables prioritization of retention efforts.

Explainable AI

Random Forest feature importance was used to identify dominant churn drivers such as revenue, recharge amounts, and usage metrics, ensuring transparency and interpretability.

Deployment-Oriented Outputs

The system generates:

Full customer churn predictions (all_customers_churn_risk.csv)

Actionable High and Medium risk customer lists (high_medium_risk_customers.csv)

An automated insight summary is also produced, containing risk distribution and top churn drivers.

Dynamic Pipeline Design

The pipeline was structured so that:

Preprocessing applies only to feature matrices (original datasets remain unchanged)

New telecom datasets with similar schema can be scored using the same workflow

Models can be retrained for new domains

Design principle:

The pipeline is reusable; the model is retrainable.

Final System Capabilities

The completed system includes:

Leakage-free ML pipeline

Exploratory analysis with correlation matrix

Logistic Regression baseline

Random Forest model

Stratified K-Fold cross-validation

Explainable feature importance

Full dataset scoring

Risk segmentation

Business-ready CSV exports

Automated insight summary generation

Conclusion

This project demonstrates a complete machine learning lifecycle, from raw data to deployment-ready churn intelligence. Emphasis was placed on engineering rigor, validation, explainability, and business usability, reflecting real-world ML development practices rather than academic modeling alone.

OUTPUT:

<img width="1536" height="759" alt="output2" src="https://github.com/user-attachments/assets/cf40a950-217d-4454-9ae3-5d5aa9a26726" />

<img width="798" height="607" alt="Screenshot 2026-02-05 110005" src="https://github.com/user-attachments/assets/609b866c-6fb6-4aef-86ee-b728038ffd39" />

