import pandas as pd
import numpy as np

def clean_vehicle_intro_date(date_str):
    if pd.isnull(date_str):
        return np.nan
    date_str = str(date_str).strip()
    
    try:
        # Case: format like '6/2002' or '06/2002' (only month/year)
        if '/' in date_str and len(date_str.split('/')) == 2 and len(date_str) <= 7:
            return pd.to_datetime("01/" + date_str, format="%d/%m/%Y")
        else:
            # Let pandas infer full datetime with hour if present
            return pd.to_datetime(date_str, infer_datetime_format=True)
    except:
        return np.nan
