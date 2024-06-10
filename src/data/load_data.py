import pandas as pd
import os


def load_csv(filepath: str) -> pd.DataFrame:
    """
    Load a CSV file into a Pandas DataFrame.

    Parameters:
    filepath (str): Path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")

    df = pd.read_csv(filepath)
    return df


def load_mzml(filepath: str):
    """
    Load an mzML file using pyteomics.

    Parameters:
    filepath (str): Path to the mzML file.

    Returns:
    pyteomics.mzml.MzML: mzML object containing the loaded data.
    """
    from pyteomics import mzml

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")

    mzml_data = mzml.read(filepath)
    return mzml_data

# TODO: Add other functions for different file formats as needed
