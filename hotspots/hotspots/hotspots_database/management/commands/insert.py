import pandas
import random
import re
import datetime
from django.db import models
#from django.contrib.auth.models import User
from hotspots_database.models import (
											GeneName,
											GrCh37,
											GrCh38)
from configparser import RawConfigParser




def insert_data(cleaned_data):
	"""Insert data into the database"""
	config = RawConfigParser()
	config.read('../credentials.ini')

	# # Get or create a legacy user
	# legacy_username = config.get('legacy', 'legacy_username')
	# legacy_password = config.get('legacy', 'legacy_password')
	# user, created = User.objects.get_or_create(username=legacy_username, email="no email")
	# if not created:
	# 	user.set_password(legacy_password)
	# user.is_superuser=False
	# user.is_staff=False
	# user.save()


	# Loop through each row
	for index, row in cleaned_data.df.iterrows():

		genes, created = GeneName.objects.get_or_create(
				gene_name = row["Hugo_Symbol"],
				hgnc_id = row["Hugo_Symbol"],
				)
				

		grch37, created = GrCh37.objects.get_or_create(
				hotspot_id = genes.hotspot_id,
				genomic_position_start_37 = row["Genomic_Position"],
    			genomic_position_end_37 = row["Genomic_Position"]
				)

		grch38, created = GrCh38.objects.get_or_create(
				hotspot_id = genes.hotspot_id,
				genomic_position_start_38 = row["Genomic_Position"],
    			genomic_position_end_38 = row["Genomic_Position"]
				)
		print(genes)
#				genomic_position_start_38 = sorted(row[no_count])[-1],
#    			genomic_position_end_38 = sorted(row[no_count])[0]