import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the DataFrame by handling missing values and duplicates.

    Parameters:
    df (pd.DataFrame): The DataFrame to clean.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    df_cleaned = df.drop_duplicates().dropna()
    return df_cleaned


def normalize_data(df: pd.DataFrame, method: str = 'z-score') -> pd.DataFrame:
    """
    Normalize the data using the specified method.

    Parameters:
    df (pd.DataFrame): The DataFrame to normalize.
    method (str): The normalization method to use ('z-score', 'min-max', etc.).

    Returns:
    pd.DataFrame: The normalized DataFrame.
    """
    if method == 'z-score':
        df_normalized = (df - df.mean()) / df.std()
    elif method == 'min-max':
        df_normalized = (df - df.min()) / (df.max() - df.min())
    else:
        raise ValueError(f"Unknown normalization method: {method}")

    return df_normalized


def filter_data(df: pd.DataFrame, threshold: float = 0.0) -> pd.DataFrame:
    """
    Filter the DataFrame by removing rows with values below the given threshold.

    Parameters:
    df (pd.DataFrame): The DataFrame to filter.
    threshold (float): The threshold value to filter the data.

    Returns:
    pd.DataFrame: The filtered DataFrame.
    """
    df_filtered = df[df >= threshold].dropna()
    return df_filtered


#TODO: Add other preprocessing functions as needed
