# 🚗 ACIS Insurance Claims Analysis

This project performs exploratory data analysis (EDA) and statistical investigation on car insurance data from **AlphaCare Insurance Solutions (ACIS)**, spanning February 2014 to August 2015. The objective is to uncover patterns, detect anomalies, and derive business insights to support underwriting decisions and risk evaluation.

---

## Project Structure
---
```
KAIM-WEEK-3/
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
## Tech Stack

**Languages & Libraries:**  
Python, Pandas, SpaCy, Scikit-learn, Hugging Face Transformers, Matplotlib, Seaborn

**Version Control:**  
Git, GitHub

**Visualization:**  
Matplotlib, Seaborn, WordCloud

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
