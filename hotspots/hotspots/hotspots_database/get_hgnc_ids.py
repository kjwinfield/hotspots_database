'''
Return HGNC IDs when the gene name is input
This will help clean up the hotspots datbase as the input file
only has gene names, and not gene IDs
'''
import requests     # Needed to talk to the API
import json         # Needed to format the ouput data
import pymysql      # Needed to access the SQL database

# Define URL information as strings
BASE_URL_FOR_HGNC = "http://rest.genenames.org/search/"
JSON_HEADER = {'Accept': 'application/json'} # Ensures JSON output

# Create empty dictionary for gene name: ID pairs
gene_names_and_hgnc_id = {}

def request_hgnc_id(base_url, header, gene_name):
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
    return response

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='kjwin',
                             password='datapass',
                             database='hotspots',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:

        # Statement to select the gene symbols from the gene table
        sql = "SELECT Hugo_Symbol FROM gene;"
        
        # Execute the statement
        cursor.execute(sql)

        # Return this info as a dictionary
        gene_names_dict = cursor.fetchall()
        #print(gene_names_dict)

        gene_names_list = []

        for i in gene_names_dict:
            gene_names_list.append(i['Hugo_Symbol'])

        for gene_name in gene_names_list:
            answer = request_hgnc_id(BASE_URL_FOR_HGNC, JSON_HEADER, gene_name)
            closest_HGNC_ID = answer['response']['docs'][0]['hgnc_id'].split(':')[1]
            gene_names_and_hgnc_id[gene_name] = closest_HGNC_ID

        # Statement to add hgnc ids to the gene table
        # Create list of tuples in format [(ID, gene_name)] to ensure executemany statement will work
        list_of_tuples = []
        for i in gene_names_and_hgnc_id.keys():
            value = gene_names_and_hgnc_id[i]
            one_tuple = (value, i)
            list_of_tuples.append(one_tuple)

        stmt = "UPDATE gene SET hgnc_id = %s WHERE (Hugo_Symbol) = %s"
        cursor.executemany(stmt, list_of_tuples)
      
    # Commit to save changes 
    connection.commit()


