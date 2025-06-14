# 🚗 ACIS Insurance Claims Analysis

This project performs exploratory data analysis (EDA) and statistical investigation on car insurance data from **AlphaCare Insurance Solutions (ACIS)**, spanning February 2014 to August 2015. The objective is to uncover patterns, detect anomalies, and derive business insights to support underwriting decisions and risk evaluation.

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
│ ├── task1_eda.ipynb # Data preprocessing notebook
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

## Tech Stack

**Languages & Libraries:**  
Python, Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn, Hugging Face, SpaCy

**Version Control:**  
Git, GitHub

**Visualization:**  
Matplotlib, Seaborn, WordCloud

**Data Management:**  
[DVC (Data Version Control)](https://dvc.org/) for dataset versioning and reproducibility

---

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
cd KAIM-WEEK-2
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
