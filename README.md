# 🛒 SmartCart Customer Segmentation

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-black)](https://flask.palletsprojects.com/)
[![Deployment](https://img.shields.io/badge/Deployed-Railway-purple)](https://railway.app/)
A machine learning-based customer segmentation system that groups e-commerce customers into meaningful segments based on their demographics, purchasing behavior, spending patterns, and engagement.

## 🚀 Live Demo

👉 [Explore the Live Web App](https://smartcart-customer-segmentation-production.up.railway.app/)

---

## 📌 Project Overview

SmartCart is a data-driven customer segmentation system designed for e-commerce platforms. 

By analyzing demographics, purchasing behavior, spending patterns, website activity, and campaign engagement, the system automatically groups customers into distinct personas. This project utilizes **unsupervised machine learning**, allowing the system to discover natural patterns in the data without relying on predefined target labels.

The final system is packaged into a **Flask web application** that lets business users input individual customer attributes to instantly predict their corresponding market segment.

---

## 🎯 Objectives

*   **Discover Patterns:** Identify meaningful, data-driven customer cohorts.
*   **Behavioral Insights:** Understand hidden trends in customer purchasing habits.
*   **Value Assessment:** Isolate high-value customers and highly responsive target audiences.
*   **Strategic Marketing:** Power highly personalized marketing and customer retention strategies.

---

## 📊 Dataset

The system processes a dataset containing **2,240 individual customer records**.

### Feature Reference Guide

| Feature | Description |
| :--- | :--- |
| **Income** | Annual customer income |
| **Age** | Customer age |
| **Recency** | Number of days since the last recorded purchase |
| **Total Spending** | Combined monetary value spent across all product categories |
| **NumDealsPurchases** | Number of purchases made using promotional deals/discounts |
| **NumWebPurchases** | Number of transactions completed through the company website |
| **NumCatalogPurchases** | Number of transactions made using mail-order catalogs |
| **NumStorePurchases** | Number of transactions made in brick-and-mortar physical stores |
| **NumWebVisitsMonth** | Total number of visits to the website within the last month |
| **Total Children** | Combined count of dependent children and teenagers in the household |
| **Tenure** | Number of days elapsed since becoming a registered customer |
| **Response** | Binary indicator of customer response to the latest marketing campaign |
| **Complain** | Binary indicator of customer complaint history |
| **Education** | Highest educational qualification reached |
| **Living With** | Current household living arrangements |

---

## ⚙️ Machine Learning Pipeline

```text
       [ Raw Customer Data ]
                 │
                 ▼
          Data Cleaning
                 │
                 ▼
        Feature Engineering
                 │
                 ▼
       Categorical Encoding
                 │
                 ▼
         Feature Scaling
                 │
                 ▼
    Principal Component Analysis (PCA)
                 │
                 ▼
      Clustering Algorithms
 (K-Means, Agglomerative, DBSCAN)
                 │
                 ▼
       [ Customer Segments ]
                 │
                 ▼
       Flask Web Application
                 │
                 ▼
        Railway Deployment
```

---

## 💻 Local Installation & Setup

Follow these steps to run the Flask web application locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/Abhijay-Jha/SmartCart-Customer-Segmentation.git
```

### 2. Navigate to the Project Directory
```bash
cd SmartCart-Customer-Segmentation
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application
```bash
python app.py
```

### 5. Access the Web App
Open your web browser and navigate to:
`http://127.0.0.1:5000`

---

## ☁️ Cloud Deployment

The production environment is continuously deployed using **Railway**.

👉 **Live Application Link:** [https://smartcart-customer-segmentation-production.up.railway.app/](https://smartcart-customer-segmentation-production.up.railway.app/)

The cloud interface lets anyone submit demographic and behavioral attributes to retrieve a cluster classification profile in real time.

---

## 📈 Future Improvements

*   **Analytics Dashboard:** Embed interactive customer analytics charts and graphics.
*   **Cluster Visualizations:** Add 2D/3D interactive PCA cluster scatter plots.
*   **Validation Metrics:** Implement rigorous cluster validation using Silhouette scores and Davies-Bouldin metrics.
*   **Actionable Insights:** Generate automated marketing and product recommendations tailored to each segment.
*   **LTV Modeling:** Integrate Customer Lifetime Value (CLV) scoring modules.
*   **Enterprise Features:** Transition to SQL database integration and user authentication.

---

## 🎓 Key Learning Outcomes

Through building this project, practical experience was gained in:

*   Advanced exploratory data analysis (EDA) and data preprocessing.
*   Dimensionality reduction using Principal Component Analysis (PCA).
*   Applying Unsupervised Learning models (**K-Means, Agglomerative Clustering, and DBSCAN**).
*   Cluster profiling and behavioral persona extraction.
*   Model serialization (`.pkl`) and integrating machine learning models into a Flask web application.
*   Cloud deployment architectures and Git workflow version control.

---

## 👨‍💻 Author

**Abhijay Jha**  
*Computer Science Student focused on Machine Learning and Data Science.*  
Passionate about designing, testing, and deploying high-utility, practical machine learning systems.
