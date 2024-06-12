import requests


# Class to interact with the string server
class StringClient:
    def __init__(self, server_url="https://string-db.org/api", output_format="tsv-no-header", method="network", species=9606, score_threshold=400):
        self.server_url = server_url
        self.output_format = output_format
        self.method = method
        self.species = species
        self.score_threshold = score_threshold

    def get_string(self):
        response = requests.get(self.server_url)
        return response.text

    # Function to map proteins to STRING IDs
    def map_proteins(self, proteins):

        request_url = f"{self.server_url}/{self.output_format}/{self.method}?identifiers={('%0d'.join(proteins))}&species={self.species}&required_score={self.score_threshold}&caller_identity=python_script"
        response = requests.get(request_url)
        response.raise_for_status()  # Ensure we notice bad responses
        return response.text
