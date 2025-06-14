import pandas as pd
import numpy as np
from scipy import stats
from typing import Dict, List, Tuple
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class InsuranceDataProcessor:
    def __init__(self, data_path: str):
        """
        Initialize the data processor with the path to the insurance data.
        
        Args:
            data_path (str): Path to the insurance data CSV file
        """
        self.data_path = data_path
        self.df = None
        
    def load_data(self) -> None:
        """Load the insurance data from CSV file."""
        try:
            self.df = pd.read_csv(self.data_path)
            logger.info(f"Successfully loaded data with shape: {self.df.shape}")
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def calculate_loss_ratio(self) -> pd.Series:
        """
        Calculate the loss ratio (TotalClaims / TotalPremium) for each record.
        
        Returns:
            pd.Series: Series containing loss ratios
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        return self.df['TotalClaims'] / self.df['TotalPremium']
        
    def analyze_by_province(self) -> pd.DataFrame:
        """
        Analyze insurance metrics by province.
        
        Returns:
            pd.DataFrame: DataFrame containing province-wise analysis
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        return self.df.groupby('Province').agg({
            'TotalPremium': 'sum',
            'TotalClaims': 'sum',
            'LossRatio': 'mean'
        }).sort_values('LossRatio', ascending=False)
        
    def analyze_by_gender(self) -> pd.DataFrame:
        """
        Analyze insurance metrics by gender.
        
        Returns:
            pd.DataFrame: DataFrame containing gender-wise analysis
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        return self.df.groupby('Gender').agg({
            'TotalPremium': 'sum',
            'TotalClaims': 'sum',
            'LossRatio': 'mean'
        })
        
    def analyze_by_vehicle_type(self) -> pd.DataFrame:
        """
        Analyze insurance metrics by vehicle type.
        
        Returns:
            pd.DataFrame: DataFrame containing vehicle type-wise analysis
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        return self.df.groupby('VehicleType').agg({
            'TotalPremium': 'sum',
            'TotalClaims': 'sum',
            'LossRatio': 'mean'
        }).sort_values('LossRatio', ascending=False)
        
    def perform_ab_test(self, group1: str, group2: str, metric: str) -> Tuple[float, float]:
        """
        Perform A/B testing between two groups for a given metric.
        
        Args:
            group1 (str): Name of the first group
            group2 (str): Name of the second group
            metric (str): Metric to compare
            
        Returns:
            Tuple[float, float]: t-statistic and p-value
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        group1_data = self.df[self.df['Province'] == group1][metric]
        group2_data = self.df[self.df['Province'] == group2][metric]
        
        t_stat, p_value = stats.ttest_ind(group1_data, group2_data)
        return t_stat, p_value
        
    def get_summary_statistics(self) -> Dict:
        """
        Get summary statistics for key metrics.
        
        Returns:
            Dict: Dictionary containing summary statistics
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        return {
            'Total Premium': self.df['TotalPremium'].sum(),
            'Total Claims': self.df['TotalClaims'].sum(),
            'Average Loss Ratio': (self.df['TotalClaims'].sum() / self.df['TotalPremium'].sum()),
            'Number of Policies': len(self.df),
            'Unique Provinces': self.df['Province'].nunique(),
            'Unique Vehicle Types': self.df['VehicleType'].nunique()
        }

if __name__ == "__main__":
    # Example usage
    processor = InsuranceDataProcessor("../data/insurance_data.csv")
    processor.load_data()
    
    # Get summary statistics
    summary = processor.get_summary_statistics()
    logger.info("Summary Statistics:")
    for key, value in summary.items():
        logger.info(f"{key}: {value}")
        
    # Analyze by province
    province_analysis = processor.analyze_by_province()
    logger.info("\nProvince Analysis:")
    logger.info(province_analysis)
    
    # Perform A/B test between two provinces
    t_stat, p_value = processor.perform_ab_test('Province1', 'Province2', 'LossRatio')
    logger.info(f"\nA/B Test Results:")
    logger.info(f"t-statistic: {t_stat:.4f}")
    logger.info(f"p-value: {p_value:.4f}") 