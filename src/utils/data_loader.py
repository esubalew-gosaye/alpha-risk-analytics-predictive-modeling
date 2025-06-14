import pandas as pd

def load_data(file_path, delimiter=","):
    """
    Load dataset from a text file with optional delimiter.

    Parameters:
    - file_path (str): Path to the .txt or .csv file.
    - delimiter (str): Delimiter used in the file (default is comma).

    Returns:
    - pd.DataFrame: Loaded dataset.
    """
    try:
        data = pd.read_csv(file_path, delimiter=delimiter)
        if "Unnamed: 0" in data.columns:
            data.drop(columns="Unnamed: 0", inplace=True)
        print(f"Data loaded successfully from {file_path}")
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: There was a parsing error while reading the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return None
