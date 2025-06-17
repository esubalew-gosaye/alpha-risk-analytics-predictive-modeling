# 🚗 ACIS Insurance Claims Analysis

This project performs an end-to-end analysis of car insurance data from **AlphaCare Insurance Solutions (ACIS)**, covering the period from February 2014 to August 2015. The goal is to uncover insights, evaluate risk and pricing fairness, and build predictive models to support dynamic, risk-based pricing.

---

## Project Objectives

- Perform **exploratory data analysis (EDA)** to identify trends, anomalies, and key business insights.
- Set up a **reproducible and auditable data pipeline** using DVC.
- Conduct **A/B testing** to evaluate risk and margin differences across customer segments.
- Build and evaluate **predictive models** for:
  - Claim **severity** (for customers who made claims)
  - Claim **frequency** (likelihood of a customer making a claim)

---


## Project Structure
---
```
KAIM-WEEK-3/
├── .dvc/ # DVC Metadata
├── .github/
│ └── workflows/ # GitHub Actions workflows
├── data/
│ ├── raw/ # Raw data (should never be modified)
│ └── processed/ # Processed/cleaned data (gitignored)
├── notebooks/
├── notebooks/
│ ├── task1_eda.ipynb # EDA and data cleaning
│ ├── task2_dvc.ipynb # DVC 
│ ├── task3_hypothesis_tesing.ipynb # A/B testing analysis
│ └── task4_ml.ipynb # Modeling for claim severity & frequency
│ └── README.md # Documentation for notebooks
├── scripts/
│ └── README.md # Documentation for scripts
├── src/
│ └── utils/ # Utility functions
    │ ├── data_loader.py # Data loading utilities
    │ ├── clean_data.py # Data preprocessing utilities
│ └── README.md # Documentation for source code
├── tests/
│ └── README.md # Testing documentation
├── .gitattributes
├── .gitignore
├── README.md # Main project documentation
└── requirements.txt # Python dependencies
```


---

## ⚙️ Tech Stack

**Languages & Libraries:**  
Python, Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn, XGBoost, SHAP, SciPy

**Data Management & Reproducibility:**  
Git, GitHub, DVC (Data Version Control)

**Statistical Analysis:**  
T-tests, ANOVA for A/B testing

**Modeling:**  
Linear Regression, Random Forest, XGBoost  
Logistic Regression and Classifiers for claim frequency  
SHAP for feature importance and interpretability

---

## Key Tasks Completed

### ✅ Task 1: Data Understanding & EDA
- Cleaned and transformed raw datasets
- Converted categorical, date, and numerical fields
- Explored trends in claims, premiums, loss ratios, and outliers
- Generated visual summaries by province, vehicle age, and more

### ✅ Task 2: Reproducible Pipeline with DVC
- Integrated DVC to version control datasets and outputs
- Set up pipeline scripts for data preprocessing and cleaning
- Enabled auditability and collaboration via remote storage and GitHub Actions

### ✅ Task 3: Statistical A/B Testing
- Analyzed differences in risk (claim frequency, severity) and margin
- Performed statistical hypothesis tests across **gender**, **province**, and **postal code**
- Identified key customer segments with significantly higher risk or profit variation

### ✅ Task 4: Predictive Modeling
- Built and evaluated models to:
  - Predict **claim severity** (TotalClaims) for claimants using RMSE and R²
  - Predict **claim frequency** using classification models (accuracy, precision, recall)
- Performed model comparison (Linear Regression, Random Forest, XGBoost)
- Applied **SHAP** to explain model predictions and identify top risk drivers

---

## Reproducible Data Pipeline with DVC

This project uses **DVC** to track and version large datasets, ensuring full reproducibility of experiments.

### Basic Workflow

```bash
# Track raw data
dvc add data/raw/claims.csv

# Set up remote (e.g., local folder or cloud)
dvc remote add -d localremote /path/to/remote

# Push data to remote storage
dvc push

# Pull data in a new environment
git pull
dvc pull


## Reproducible Data Pipeline with DVC

To ensure full reproducibility and auditability — especially critical in financial and insurance sectors — this project integrates **DVC** to version and track datasets.

### DVC Highlights

- Track large datasets without bloating Git
- Version control for `.csv`, `.parquet`, or any binary files
- Local or cloud storage support
- Seamless integration with Git for team collaboration

### Basic Usage

```bash
# Initialize DVC (already done in this repo)
dvc init

# Add data to DVC
dvc add data/raw/data.csv

# Set up remote storage 
dvc remote add -d localremote /path/to/storage

# Push data to remote
dvc push

# Commit metadata to Git
git add data/raw/claims_data.csv.dvc .gitignore
git commit -m "feat: track dataset with DVC"
```
To reproduce the same data version later:

```bash

git pull
dvc pull
```
---
## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/she-code/KAIM-WEEK-3.git
cd KAIM-WEEK-3
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```
3. **Install dependencies:**

```bash
pip install -r requirements.txt

```

## Contributors
- Frehiwot Abebie
