import pandas as pd
from scipy import stats

def differential_expression_analysis(df: pd.DataFrame):
    """
    Perform differential expression analysis on a DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame with the first column "protein" and subsequent columns representing different samples.

    Returns:
    pd.DataFrame: DataFrame with p-values of the t-test for each protein.
    """
    # Initialize a dictionary to store the results
    results = {"protein": [], "p_value": []}

    # Iterate over each row (protein) in the DataFrame
    for index, row in df.iterrows():
        # Perform a t-test between the first and second sample
        t_stat, p_value = stats.ttest_ind(row[1:], row[2:])

        # Store the protein name and the p-value of the t-test
        results["protein"].append(row["protein"])
        results["p_value"].append(p_value)

    # Convert the results to a DataFrame
    results_df = pd.DataFrame(results)

    return results_df



