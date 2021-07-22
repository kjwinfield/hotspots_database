'''
Return HGNC IDs when the gene name is input
This will help clean up the hotspots datbase as the input file
only has gene names, and not gene IDs
'''
import requests     # Needed to talk to the API
import json         # Needed to format the ouput data
from configparser import RawConfigParser

# Define URL information as strings
BASE_URL_FOR_HGNC = "http://rest.genenames.org/search/"
JSON_HEADER = {'Accept': 'application/json'} # Ensures JSON output

def request_hgnc_id(gene_name, base_url=BASE_URL_FOR_HGNC, header=JSON_HEADER):
    '''
    Accesses the HGNC API for a given gene name and returns the most
    likely HGNC ID for that gene name
    parameters: base_url (str) = the url for the API
            gene_name (str) = the query gene name
    returns: an HGNC ID
    '''
    url = base_url + gene_name
    str(url)
    response = requests.get(url, headers=header)
    
    #Convert to JSON
    response = response.json()

    #Extract nearest ID
    
    nearest_id = response['response']['docs'][0]['hgnc_id'].split(':')[1]

    return nearest_id
