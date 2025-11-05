# 🔐 Machine Learning for Cybersecurity
## Malicious URL Detection & Intrusion Detection System (IDS)

**Author:** Mohamed Lamine OULAD SAID  
**Date:** November 2025  
**Environment:** Google Colab / Jupyter Notebook  
**Language:** Python 3.10+  
**Libraries:** pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn, joblib  

---

## 📘 Overview

This repository contains two machine learning projects focused on **cybersecurity**:

1. **Malicious URL Detection** – Classifies URLs as *malicious* or *benign* based on lexical and structural features.  
2. **Intrusion Detection System (IDS)** – Detects network intrusions using the **NSL-KDD dataset**, applying several supervised learning models.

Both experiments follow the same pipeline:
- Data loading and cleaning  
- Feature extraction and encoding  
- Exploratory Data Analysis (EDA)  
- Model training and evaluation  
- Comparative analysis and conclusions  

---

## 🧩 1. Malicious URL Detection

**File:** `Malicious_URLs.ipynb`  
**Objective:** Detect malicious websites based on URL characteristics.

### 🧱 Main Steps
1. **Data Preprocessing** – Clean dataset, remove duplicates, handle missing values.  
2. **Feature Engineering** – Extract lexical and structural features (length, digits, special characters, etc.).  
3. **Model Training** – Train ML models (Random Forest, XGBoost, Logistic Regression).  
4. **Evaluation** – Compare accuracy, precision, recall, and F1-score.  
5. **Result** – Save best-performing model with joblib.

---

## 🛡️ 2. Intrusion Detection System (IDS)

**File:** `TP_IDS-ML.ipynb`  
**Objective:** Detect different types of network attacks using NSL-KDD dataset.

### 🧱 Main Steps
1. **Dataset Loading** – Import KDDTrain+ and KDDTest+ datasets.  
2. **Preprocessing** – Encode categorical features, normalize numerical values.  
3. **Feature Selection** – Choose relevant features to reduce dimensionality.  
4. **Model Training** – Apply Logistic Regression, Decision Tree, Random Forest, and XGBoost.  
5. **Evaluation** – Generate confusion matrix, classification report, and accuracy metrics.

---

## 🧾 Results Summary

- **Malicious URL Detection:** ~95% accuracy using Random Forest  
- **IDS Models:** ~98% accuracy with Random Forest and XGBoost  

---

## ⚙️ Requirements

- Python 3.10+  
- pandas  
- numpy  
- scikit-learn  
- xgboost  
- seaborn  
- matplotlib  
- joblib  

---

## 🚀 Usage

1. Open notebooks in **Google Colab** or **Jupyter Notebook**.  
2. Run all cells sequentially to reproduce the experiments.  
3. Trained models will be saved in the working directory.

---

## 📊 References

- NSL-KDD Dataset: https://www.unb.ca/cic/datasets/nsl.html  
- Kaggle Malicious URLs Dataset  
- Scikit-learn and XGBoost documentation  
