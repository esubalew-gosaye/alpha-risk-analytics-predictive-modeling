import pytest
import pandas as pd
import numpy as np
from scripts.data_processor import InsuranceDataProcessor

@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    data = {
        'Province': ['Province1', 'Province2', 'Province1', 'Province2'],
        'Gender': ['M', 'F', 'M', 'F'],
        'VehicleType': ['Sedan', 'SUV', 'Sedan', 'SUV'],
        'TotalPremium': [1000, 1200, 1100, 1300],
        'TotalClaims': [500, 600, 550, 650]
    }
    return pd.DataFrame(data)

@pytest.fixture
def processor(tmp_path, sample_data):
    """Create a processor instance with sample data."""
    # Save sample data to temporary file
    data_path = tmp_path / "test_data.csv"
    sample_data.to_csv(data_path, index=False)
    
    # Create processor instance
    processor = InsuranceDataProcessor(str(data_path))
    processor.load_data()
    return processor

def test_load_data(processor, sample_data):
    """Test data loading functionality."""
    assert processor.df is not None
    assert processor.df.shape == sample_data.shape
    assert all(processor.df.columns == sample_data.columns)

def test_calculate_loss_ratio(processor):
    """Test loss ratio calculation."""
    loss_ratios = processor.calculate_loss_ratio()
    assert len(loss_ratios) == len(processor.df)
    assert all(loss_ratios >= 0)
    assert all(loss_ratios <= 1)

def test_analyze_by_province(processor):
    """Test province-wise analysis."""
    analysis = processor.analyze_by_province()
    assert 'TotalPremium' in analysis.columns
    assert 'TotalClaims' in analysis.columns
    assert 'LossRatio' in analysis.columns
    assert len(analysis) == processor.df['Province'].nunique()

def test_analyze_by_gender(processor):
    """Test gender-wise analysis."""
    analysis = processor.analyze_by_gender()
    assert 'TotalPremium' in analysis.columns
    assert 'TotalClaims' in analysis.columns
    assert 'LossRatio' in analysis.columns
    assert len(analysis) == processor.df['Gender'].nunique()

def test_analyze_by_vehicle_type(processor):
    """Test vehicle type-wise analysis."""
    analysis = processor.analyze_by_vehicle_type()
    assert 'TotalPremium' in analysis.columns
    assert 'TotalClaims' in analysis.columns
    assert 'LossRatio' in analysis.columns
    assert len(analysis) == processor.df['VehicleType'].nunique()

def test_perform_ab_test(processor):
    """Test A/B testing functionality."""
    t_stat, p_value = processor.perform_ab_test('Province1', 'Province2', 'LossRatio')
    assert isinstance(t_stat, float)
    assert isinstance(p_value, float)
    assert 0 <= p_value <= 1

def test_get_summary_statistics(processor):
    """Test summary statistics calculation."""
    summary = processor.get_summary_statistics()
    assert isinstance(summary, dict)
    assert 'Total Premium' in summary
    assert 'Total Claims' in summary
    assert 'Average Loss Ratio' in summary
    assert 'Number of Policies' in summary
    assert 'Unique Provinces' in summary
    assert 'Unique Vehicle Types' in summary

def test_error_handling():
    """Test error handling for invalid data path."""
    processor = InsuranceDataProcessor("nonexistent_file.csv")
    with pytest.raises(Exception):
        processor.load_data() 