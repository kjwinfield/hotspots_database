import numpy as np
import pandas
from pandas import read_excel
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

# Credentials to database connection
hostname="127.0.0.1"
dbname="hotspots"
uname="kjwinfield"
pwd="datapass"

#from datetime import datetime
#from models import HugoSymbol

# Takes database file (saved in hotspots_database)
filename = "./hotspots_v2.xls"

# convert excel file to dataframe
df = read_excel(filename)
#print(dataframe)
#df

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))
# Create SQLAlchemy engine to connect to MySQL Database
# engine = create_engine("mysql+pymysql://{host}/{db}".format(host=hostname, db=dbname)
# engine = create_engine('mysql://root:@127.0.0.1/hotspots')

# Convert dataframe to sql table
df.to_sql('hotspots', con=engine, index=False)
