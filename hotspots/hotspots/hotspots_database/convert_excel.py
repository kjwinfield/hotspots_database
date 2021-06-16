import numpy as np
import pandas
from pandas import read_excel
from sqlalchemy import create_engine
import pymysql
#from split_by_delimiter.sql import SplitValueIntoMultipleRows
pymysql.install_as_MySQLdb()

# Credentials to database connection
hostname="127.0.0.1"
dbname="hotspots"
uname="kjwin"
pwd="datapass"

#from datetime import datetime
#from models import HugoSymbol

# Takes database file (saved in hotspots_database)
filename = "./hotspots_v2.xls"
samplefile =  "./sample_of_db.ods"
# convert excel file to dataframe
df = read_excel(filename)
#print(dataframe)
#print(df)

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table
df.to_sql('hotspots', if_exists='replace', con=engine, index=False)
#splitting strings procedure:

# Connect to the datapass
connection = pymysql.connect(host='localhost',
                             user='kjwin',
                             password='datapass',
                             database='hotspots',
                             cursorclass=pymysql.cursors.DictCursor)

# '''
# Create tables
# '''
# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "CREATE TABLE IF NOT EXISTS amino_acid_change AS SELECT Variant_Amino_Acid, Mutation_Count FROM hotspots"
#         cursor.execute(sql)
#     connection.commit()

'''
Splitting the rows with | as a delimiter
'''
with connection:
    with connection.cursor() as cursor:
        sql = "CREATE TABLE IF NOT EXISTS amino_acid_change AS SELECT Variant_Amino_Acid, Mutation_Count FROM hotspots"
        cursor.execute(sql)

        # Create a new record
        # sql = "SELECT id, substring_index(substring_index(Samples, '|', 1), '|', -1) AS sample_type FROM samples"
        # cursor.execute(sql)
        # result = cursor.fetchall()
        # print(result)

        # Call procedure SplitValue... which will split a single row into many rows, with '|' as the delimiter
        cursor.callproc('SplitValueIntoMultipleRows')

        # Return this info as a dictionary
        sample_type_dict = cursor.fetchall()
        
        # Call procedure SplitValue... which will split a single row into many rows, with '|' as the delimiter
        cursor.callproc('SplitValueIntoMultipleRowsCodonChange')

        # Return this info as a dictionary
        codon_change_dict = cursor.fetchall()

    # Commit to save changes 
    connection.commit()

# Create new dataframe from dictionary
df2 = pandas.DataFrame.from_dict(sample_type_dict)
df2.to_sql('sample_types', engine, if_exists='replace', index='new_id') # Convert this dataframe to SQL table

# Create new dataframe from dictionary
df3 = pandas.DataFrame.from_dict(codon_change_dict)
df3.to_sql('nucleotide_changes', engine, if_exists='replace', index='new_id') # Convert this dataframe to SQL table
