# Notebooks

This folder contains Jupyter notebooks demonstrating the usage and exploration of the data preprocessing module.

## : task_1_data_understanding_eda.py

- Loading and inspecting the dataset

- Updates datatypes of columns

- Handling missing values and removing duplicates

- Statistical summaries using describe() and variability checks

- Univariate analysis using histograms and bar charts

- Bivariate and multivariate analysis (e.g., correlations, scatter plots by region)

- Outlier detection using box plots

- Categorical comparisons across provinces

- Creative visualizations to highlight key insights

- Loss ratio analysis and trends across geography and time

## : task_2_dvc.py

- Initalizes dvc

- creates localstorage | localremote

- adds files to dvc

- tracks files

- pushes file to localremote
 
## : task3_hypothesis_testing.py

- Computes claim frequency and severity

- Defines and executes A/B hypothesis tests

- Tests risk differences across provinces using ANOVA

- Tests claim severity differences across postal codes

- Tests margin (profit) difference across postal codes using t-test

- Tests risk difference between genders using chi-squared test

- Provides statistical decision (reject/fail to reject H₀)

- Adds business interpretation for each test result


## Running Notebooks

To run the notebooks:

1. Install required dependencies (see `requirements.txt`).
2. Launch Jupyter Notebook or JupyterLab:

```bash
jupyter notebook
```