import requests


class UniprotClient:
    # init function
    def __init__(self, server_url="https://rest.uniprot.org/uniprotkb/", verbose=False):
        self.base_url = "https://rest.uniprot.org/uniprotkb/"
        self.base_uniparc_url = "https://rest.uniprot.org/uniparc/"
        self.base_unisave_url = "https://rest.uniprot.org/unisave/"
        self.verbose = verbose

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
                return gene_name
            except (IndexError, KeyError):
                if self.verbose:
                    print(f"No data found in Uniprot for protein ID {protein_id}. Returning 'None ({protein_id})'.")
                return f"None ({protein_id})"
        else:
            if self.verbose:
                print(f"Error fetching data in UniProt for protein ID {protein_id}: {response.status_code}. Returning Null value.")
            return None

    def get_gene_name_from_uniparc(self, protein_id):
        """
        Given a Uniparc protein ID, fetch the corresponding gene name using the UniProt API.

        Args:
        protein_id (str): The Uniparc protein ID.

        Returns:
        str: The gene name corresponding to the given protein ID. If not found, returns None.
        """

        url = f"{self.base_uniparc_url}{protein_id}.json"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            try:
                gene_name = data['genes'][0]['geneName']['value']
                return gene_name
            except (IndexError, KeyError):
                if self.verbose:
                    print(f"No data found in Uniparc for protein ID {protein_id}. Returning 'None ({protein_id})'.")
                return f"None ({protein_id})"
        else:
            if self.verbose:
                print(f"Error fetching data in Uniparc for protein ID {protein_id}: {response.status_code}. Returning Null value.")
            return None

    def get_gene_name_from_unisave(self, protein_id):
        """
        Given a Unisave protein ID, fetch the corresponding gene name using the Unisave API.

        Args:
        protein_id (str): The UniProt protein ID.

        Returns:
        str: The gene name corresponding to the given protein ID. If not found, returns None.
        """

        url = f"{self.base_unisave_url}{protein_id}?format=txt"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.text

            try:
                gene_name = None
                found = False

                lines = data.split('\n')
                index = 0
                while not found and index < len(lines):
                    current_line = lines[index]
                    if current_line.startswith("GN   Name="):
                        gene_name = current_line.split('=')[1].split(';')[0].strip()

                        # if gene_name contains { take the first part and trim it
                        if "{" in gene_name:
                            gene_name = gene_name.split("{")[0].strip()

                        found = True
                    index += 1

                if self.verbose:
                    print(f"Gene name found in Unisave: {gene_name}.")

                return gene_name
            except (IndexError, KeyError):
                if self.verbose:
                    print(f"No data found in Unisave for protein ID {protein_id}. Returning 'None ({protein_id})'.")
                return f"None ({protein_id})"
        else:
            if self.verbose:
                print(f"Error fetching data in Unisave for protein ID {protein_id}: {response.status_code}. Returning Null value.")
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

            # if gene_name is not null
            if gene_name is not None:
                # If not found with UniProt, try with Uniparc
                if gene_name.startswith("None ("):
                    gene_name = self.get_gene_name_from_unisave(protein_id)

            result[protein_id] = gene_name
        return result

# Example usage:
# protein_ids = ['P12345', 'Q8N158', 'P04637']
# gene_names = batch_translate_protein_ids(protein_ids)
# print(gene_names)
