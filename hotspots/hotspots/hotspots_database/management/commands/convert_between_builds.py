'''
Script to use Ensembl Rest API to convert the coordinates
of the cancer hotspots database from GRCh37 to GRCh38
'''
import requests     # Needed to talk to the API
import json         # Needed to format the ouput data
from os import path # Needed to access the bed file of grch37 coordinates

# Define all the URL information as strings
ENSEMBL_BASE_URL = "https://rest.ensembl.org/"
JSON_HEADER = {'Content-Type': 'application/json'} #Ensures output is JSON

def convert_to_grch38(base_url, coordinates, header, species="human", current_build="GRCh37", build_to_convert_to="GRCh38"):
    '''
    Accesses the Ensembl API and converts between builds
    parameters: base_url (str) = the url for the API
                coordinates (list) = formatted e.g. [4, 152329754, 152329755]
    returns: a list of lists of grch38 coordinates 
    '''
    answer_list = []
    for coordinate in coordinates:
        coordinate_string = coordinate[0] + ':' + coordinate[1] + '..' + coordinate[2]
        url = base_url + '/map/' + species + '/' + current_build + '/' + coordinate_string + '/' + build_to_convert_to
        str(url)
        response = requests.get(url, headers=header)
        
        #Convert to JSON
        response = response.json()
        # Select the useful parts of the response
        # Returns a list in formatted e.g. [16, 67610833, 67610835]
        chr_on_38 = response['mappings'][0]['mapped']['seq_region_name']
        start_on_38 = response['mappings'][0]['mapped']['start']
        end_on_38 = response['mappings'][0]['mapped']['end']
        answer = [chr_on_38, start_on_38, end_on_38]
        answer_list.append(answer)

    return answer_list

# Apply this funciton to the bed file

basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "..","..", "..", "grch37_coordinates.bed"))

with open(filepath) as f:
    content = f.readlines()
# Remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

all_coordinates_list = []

for i in content:
    empty_list = []
    # Split bed file by tabs and strip 'chr' from chromosome number
    empty_list.append(i.split('\t')[0].strip('chr'))
    empty_list.append(i.split('\t')[1])
    empty_list.append(i.split('\t')[2])
    all_coordinates_list.append(empty_list)

grch38_coordinates = convert_to_grch38(ENSEMBL_BASE_URL, all_coordinates_list, JSON_HEADER)
test_coordinates = ['16', '56873495', '56873495']
test_coord_2 = ['8', '145738768', '145738768']
test_coordinates_list = [test_coordinates, test_coord_2]
#tested_coordinates = convert_to_grch38(ENSEMBL_BASE_URL, test_coordinates_list, JSON_HEADER)