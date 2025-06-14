
import pandas as pd
import os
import pytest
import sys
import numpy as np
from datetime import datetime
import warnings

# Suppress specific pandas warnings
warnings.filterwarnings("ignore", 
                       category=UserWarning,
                       message="The argument 'infer_datetime_format' is deprecated")
warnings.filterwarnings("ignore",
                       category=UserWarning,
                       message="Parsing dates in %d/%m/%Y format when dayfirst=False")

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.clean_data import clean_vehicle_intro_date

@pytest.mark.parametrize("input_date,expected", [
    # Valid month/year formats
    ('6/2002', datetime(2002, 6, 1)),
    ('06/2002', datetime(2002, 6, 1)),
    ('12/2020', datetime(2020, 12, 1)),
    
    # Valid date formats
    ('2020-06-15', datetime(2020, 6, 15)),
    ('15/06/2020', datetime(2020, 6, 15)),
    ('06/15/2020', datetime(2020, 6, 15)),
    
    # Datetime with time components (will compare date only)
    ('2020-06-15 14:30:00', datetime(2020, 6, 15)),
    
    # Edge cases
    ('2/1999', datetime(1999, 2, 1)),
    ('02/1999', datetime(1999, 2, 1)),
    ('1/1/2020', datetime(2020, 1, 1)),
    ('2020-01-01 00:00:00', datetime(2020, 1, 1)),
    
    # Invalid cases
    ('invalid', pd.NA),
    ('13/2020', pd.NA),  # Invalid month
    ('6/20020', pd.NA),  # Invalid year
    (None, pd.NA),
    (np.nan, pd.NA),
    ('', pd.NA),
    (' ', pd.NA),
])
def test_clean_vehicle_intro_date(input_date, expected):
    result = clean_vehicle_intro_date(input_date)
    
    if pd.isna(expected):
        assert pd.isna(result)
    else:
        # Convert both to date objects for comparison
        if hasattr(result, 'date'):
            result_date = result.date()
        else:
            result_date = result
            
        if hasattr(expected, 'date'):
            expected_date = expected.date()
        else:
            expected_date = expected
            
        assert result_date == expected_date