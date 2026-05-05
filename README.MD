# 🏦 LoanRisk AI - Smart Loan Approval & Risk Assessment System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red)
![ML](https://img.shields.io/badge/Machine-Learning-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Project Overview

LoanRisk AI is an intelligent **FinTech application** that predicts loan approval status and assesses risk levels using Machine Learning algorithms. The system helps financial institutions make faster, data-driven lending decisions.

### 🎯 Key Features

- ✅ **Instant Loan Approval Prediction** (Approve/Reject)
- 📊 **Risk Assessment** (Low/Medium/High)
- 🤖 **Multiple ML Models** (Random Forest, XGBoost, Logistic Regression)
- 📈 **90%+ Accuracy** on Risk Prediction
- 🎨 **Interactive Web Interface** built with Streamlit
- 🔄 **Real-time Predictions**

---

## 📊 Model Performance

| Model | Task | Accuracy | F1-Score |
|-------|------|----------|----------|
| Random Forest | Loan Approval | 63.4% | 73.7% |
| Decision Tree | Risk Prediction | 90.2% | 89.8% |

---

## 🏗️ Project Structure
LoanRisk-AI/
│
├── app.py # Streamlit web application
├── final_model1.pkl # Loan Approval Model
├── final_model2.pkl # Risk Prediction Model
├── scaler.pkl # StandardScaler for features
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
├── README.md # Project documentation
├── train.csv # Training dataset
├── test.csv # Testing dataset
└── Loan risk prediction.ipynb # Jupyter notebook with EDA & training


---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/LoanRisk-AI.git
cd LoanRisk-AI