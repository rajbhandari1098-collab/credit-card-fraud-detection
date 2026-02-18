# 💳 Credit Card Fraud Detection Web App

A Machine Learning based web application that detects fraudulent credit card transactions using Logistic Regression.  
This project includes model training, data preprocessing, and deployment using Flask.

---

## 📌 Project Overview

Credit card fraud is a major issue in financial systems.  
This project builds a classification model to detect whether a transaction is:

- ✅ Normal Transaction
- ❌ Fraud Transaction

The dataset is highly imbalanced, so undersampling was used to balance the classes before training.

---

## 📊 Dataset Information

- Dataset Name: Credit Card Fraud Detection
- Source: Kaggle
- Total Transactions: 284,807
- Fraud Cases: 492
- Features: 30 (Time, V1–V28, Amount)
- Target Column: Class (0 = Normal, 1 = Fraud)

🔗 Dataset Link:  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

---

## ⚙️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-Learn
- Flask
- HTML
- CSS

---

## 🧠 Machine Learning Model

- Algorithm: Logistic Regression
- Data Balancing Technique: Random Undersampling
- Train-Test Split: 80% Training / 20% Testing
- Evaluation Metric: Accuracy Score

---

## 📁 Project Structure

