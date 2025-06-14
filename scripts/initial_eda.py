# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from scipy import stats

# Set plot style
plt.style.use('seaborn')
sns.set_palette('husl')

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Load the dataset
df = pd.read_csv('../data/insurance_data.csv')

# Display basic information
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData Types:")
print(df.dtypes)
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100

# Create a DataFrame to display missing values
missing_df = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage': missing_percentage
})

# Sort by percentage of missing values
missing_df = missing_df.sort_values('Percentage', ascending=False)
print("\nMissing Values Analysis:")
print(missing_df[missing_df['Missing Values'] > 0])

# Calculate Loss Ratio
df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']

# Analyze by province
province_analysis = df.groupby('Province').agg({
    'TotalPremium': 'sum',
    'TotalClaims': 'sum',
    'LossRatio': 'mean'
}).round(2)

print("\nProvince-wise Analysis:")
print(province_analysis)

# Visualize average loss ratio by province
plt.figure(figsize=(12, 6))
sns.barplot(x=province_analysis.index, y='LossRatio', data=province_analysis.reset_index())
plt.title('Average Loss Ratio by Province')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Convert TransactionMonth to datetime
df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])

# Aggregate monthly metrics
monthly_metrics = df.groupby('TransactionMonth').agg({
    'TotalPremium': 'sum',
    'TotalClaims': 'sum',
    'LossRatio': 'mean'
}).reset_index()

# Plot monthly trends
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Premium and Claims
ax1.plot(monthly_metrics['TransactionMonth'], monthly_metrics['TotalPremium'], label='Premium')
ax1.plot(monthly_metrics['TransactionMonth'], monthly_metrics['TotalClaims'], label='Claims')
ax1.set_title('Monthly Premium and Claims')
ax1.legend()
ax1.tick_params(axis='x', rotation=45)

# Loss Ratio
ax2.plot(monthly_metrics['TransactionMonth'], monthly_metrics['LossRatio'])
ax2.set_title('Monthly Loss Ratio')
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

# Analyze vehicle makes with highest claim amounts
vehicle_analysis = df.groupby('VehicleMake').agg({
    'TotalClaims': 'sum',
    'TotalPremium': 'sum',
    'LossRatio': 'mean'
}).sort_values('TotalClaims', ascending=False)

print("\nTop 10 Vehicle Makes by Total Claims:")
print(vehicle_analysis.head(10))

# Visualize top 10 vehicle makes by claims
plt.figure(figsize=(12, 6))
sns.barplot(x=vehicle_analysis.head(10).index, y='TotalClaims', data=vehicle_analysis.head(10).reset_index())
plt.title('Top 10 Vehicle Makes by Total Claims')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Analyze risk by gender
gender_analysis = df.groupby('Gender').agg({
    'TotalPremium': 'sum',
    'TotalClaims': 'sum',
    'LossRatio': 'mean'
}).round(2)

print("\nRisk Analysis by Gender:")
print(gender_analysis)

# Visualize gender-based risk
plt.figure(figsize=(8, 6))
sns.barplot(x=gender_analysis.index, y='LossRatio', data=gender_analysis.reset_index())
plt.title('Average Loss Ratio by Gender')
plt.tight_layout()
plt.show() 