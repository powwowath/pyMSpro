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

import requests
import time


# Function to map UniProt IDs to protein names
def map_uniprot_ids_to_names(protein_ids):
    # Prepare the URL and the query parameters
    url = 'https://rest.uniprot.org/idmapping/run'
    params = {
        'from': 'UniProtKB_AC-ID',  # Input ID type
        'to': 'UniProtKB',  # Output ID type
        'ids': ','.join(protein_ids)  # List of protein IDs
    }

    # Send the request to start the mapping job
    response = requests.post(url, data=params)
    response.raise_for_status()

    # Extract the job ID from the response
    job_id = response.json()['jobId']

    # Check the status of the job until it is completed
    status_url = f'https://rest.uniprot.org/idmapping/status/{job_id}'
    ret_s = ""
    while True:
        status_response = requests.get(status_url)
        status_response.raise_for_status()
        status_data = status_response.json()
        ret_s = status_data
        break
        if 'jobStatus' in status_data and status_data['jobStatus'] == 'FINISHED':
            break

        time.sleep(3)  # Wait for 3 seconds before checking again

    # Get the results of the mapping job
    results_url = f'https://rest.uniprot.org/idmapping/results/{job_id}'
    results_response = requests.get(results_url)
    results_response.raise_for_status()
    results_data = results_response.json()

    # Extract the mappings from the results
    mapped_ids = [item['to'] for item in results_data['results']]

    return mapped_ids, ret_s


# Function to get protein names using UniProt IDs
def get_protein_names(mapped_ids):
    # Prepare the URL and the query parameters
    url = 'https://rest.uniprot.org/uniprotkb/search'
    params = {
        'query': ' '.join(mapped_ids),
        'fields': 'accession,protein_name',
        'format': 'json',
        'size': len(mapped_ids)
    }

    # Send the request to get protein names
    response = requests.get(url, params=params)
    response.raise_for_status()

    # Parse the response JSON to extract protein names
    proteins = response.json()['results']
    protein_id_to_name = {
        protein['primaryAccession']: protein['proteinDescription']['recommendedName']['fullName']['value'] for protein
        in proteins}

    return protein_id_to_name










from urllib.parse import urljoin

# Define the UniProt API URL
UNIPROT_API_URL = "https://rest.uniprot.org/uniprotkb"

def get_protein_name(protein_id):
  """
  Fetches the protein name for a given ID from the UniProt API.

  Args:
      protein_id (str): The UniProt ID of the protein.

  Returns:
      str: The protein name (full name) or None if not found.
  """
  # Construct the API endpoint URL
  url = urljoin(UNIPROT_API_URL, f"{protein_id}.json")

  # Send GET request to the API
  response = requests.get(url)

  # Check for successful response
  if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Extract the protein name from the response
    return data.get("protein", {}).get("recommendedName", {}).get("fullName")
  else:
    print(f"Error retrieving protein name for ID: {protein_id} (Status Code: {response.status_code})")
    return None

def get_protein_names(protein_ids):
  """
  Retrieves protein names for a list of IDs from the UniProt API.

  Args:
      protein_ids (list): A list of UniProt protein IDs.

  Returns:
      list: A list of protein names corresponding to the IDs.
  """
  protein_names = []
  for protein_id in protein_ids:
    name = get_protein_name(protein_id)
    if name:
      protein_names.append(name)
  return protein_names



# Example usage
#protein_ids = ["P0A3A4", "Q99490", "A0A075B716"]  # Replace with your list
#protein_names = get_protein_names(protein_ids)

#print(f"Protein names:")
#for name in protein_names:
#  print(name)
