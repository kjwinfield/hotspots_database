import pymysql      # Needed to access the SQL database

connection = pymysql.connect(host='localhost',
                             user='kjwin',
                             password='datapass',
                             database='hotspots',
                             cursorclass=pymysql.cursors.DictCursor)

gene_names_and_hgnc_id = {'NRAS': '7989', 'PIK3CA': '8975', 'IDH1': '5382', 'BRAF': '1097'}

values = [[item] for item in gene_names_and_hgnc_id.values()]
keys = [[item] for item in gene_names_and_hgnc_id.keys()]




print(list_of_tuples)

with connection:
    with connection.cursor() as cursor:


      
    # Commit to save changes 
    connection.commit()
