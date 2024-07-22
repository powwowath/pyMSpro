import requests


class UniprotClient:
    # init function
    def __init__(self, server_url="https://rest.uniprot.org/uniprotkb/"):
        self.base_url = "https://rest.uniprot.org/uniprotkb/"

    def get_gene_name_from_uniprot(self, protein_id):
        """
        Given a UniProt protein ID, fetch the corresponding gene name using the UniProt API.

        Args:
        protein_id (str): The UniProt protein ID.

        Returns:
        str: The gene name corresponding to the given protein ID. If not found, returns None.
        """

        url = f"{self.base_url}{protein_id}.json"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Try to find the gene name in the JSON response
            try:
                gene_name = data['genes'][0]['geneName']['value']
                return gene_name + " (" + protein_id + ")"
                #return gene_name
            except (IndexError, KeyError):
                return "None (" + protein_id + ")"
                #return "None_" + protein_id
        else:
            print(f"Error fetching data for protein ID {protein_id}: {response.status_code}")
            return None

    def batch_translate_protein_ids(self, protein_ids):
        """
        Given a list of UniProt protein IDs, fetch the corresponding gene names.

        Args:
        protein_ids (list of str): A list of UniProt protein IDs.

        Returns:
        dict: A dictionary with protein IDs as keys and gene names as values.
        """
        result = {}
        for protein_id in protein_ids:
            gene_name = self.get_gene_name_from_uniprot(protein_id)
            result[protein_id] = gene_name
        return result

# Example usage:
#protein_ids = ['P12345', 'Q8N158', 'P04637']
#gene_names = batch_translate_protein_ids(protein_ids)
#print(gene_names)
