import requests
import logging


# Class to interact with the string server
class StringClient:
    def __init__(self, server_url="https://string-db.org/api", species=9606, score_threshold=400):
        self.server_url = server_url
        self.species = species
        self.score_threshold = score_threshold

        # log to a file
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.FileHandler("string_client.log"))

    # Function to map proteins to STRING IDs
    def map_proteins(self, proteins, output_format):

        request_url = f"{self.server_url}/{output_format}/network?identifiers={('%0d'.join(proteins))}&species={self.species}&required_score={self.score_threshold}&caller_identity=python_script"
        response = requests.get(request_url)
        response.raise_for_status()  # Ensure we notice bad responses
        return response.text

    # Function to get the functional enrichment of a list of proteins
    def get_enrichment(self, proteins, output_format):
        if type(proteins) is not list:
            proteins = [proteins]
        request_url = f"{self.server_url}/{output_format}/enrichment?identifiers={('%0d'.join(proteins))}&species={self.species}&caller_identity=python_script&output_format={output_format}"
        response = requests.get(request_url)
        response.raise_for_status()  # Ensure we notice bad responses
        return response.text

    # Function to get the link to the protein page
    def get_protein_page(self, proteins, output_format):
        if type(proteins) is not list:
            proteins = [proteins]
        request_url = f"{self.server_url}/{output_format}/get_link?identifiers={('%0d'.join(proteins))}&species={self.species}"
        response = requests.get(request_url)
        response.raise_for_status()  # Ensure we notice bad responses
        return response.text

    # Function to get the functional annotations of a list of proteins
    def get_annotations(self, proteins, output_format):
        if type(proteins) is not list:
            proteins = [proteins]
        request_url = f"{self.server_url}/{output_format}/functional_annotation?identifiers={('%0d'.join(proteins))}&species={self.species}&caller_identity=python_script&output_format={output_format}"
        response = requests.get(request_url)
        response.raise_for_status()  # Ensure we notice bad responses
        return response.text
    
    # Function to get the protein interactions
    def get_interactions(self, proteins, output_format):
        if type(proteins) is not list:
            proteins = [proteins]
        request_url = f"{self.server_url}/{output_format}/interaction_partners?identifiers={('%0d'.join(proteins))}&species={self.species}&caller_identity=python_script&output_format={output_format}"
        response = requests.get(request_url)
        response.raise_for_status()  # Ensure we notice bad responses
        return response.text

    # Function to get the image of the Network
    def get_network_image(self, proteins, output_format):
        if type(proteins) is not list:
            proteins = [proteins]
        request_url = f"{self.server_url}/{output_format}/network?identifiers={('%0d'.join(proteins))}&species={self.species}&caller_identity=python_script&output_format={output_format}"
        response = requests.get(request_url)
        response.raise_for_status()  # Ensure we notice bad responses
        return response.content