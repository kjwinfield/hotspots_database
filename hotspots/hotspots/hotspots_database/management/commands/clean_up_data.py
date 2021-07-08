
import pandas as pd
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta
from hotspots_database.management.commands.convert_between_builds import grch38_coordinates
from hotspots_database.management.commands.add_hgnc_ids import request_hgnc_id

class Data:
	def __init__(self, data_path):
		self.read_data_into_df(data_path)

	def read_data_into_df(self, path):
		data_df = pd.read_excel(path)
		self.df = data_df

    
	def remove_mutation_count_from_position_and_sort(self):
		'''
		Currently the genome positions are stored in the format 4:153250882_3
		where the _3 is the count of samples with a mutation at that position.
		This is very unhelpful so this function strips off the count from the
		genomic position

		It then returns a sorted list of the genome positions 
		'''
		
		for index, row in self.df.iterrows():
			no_count = []
			value = row["Genomic_Position"]
			split_value = value.split('|')
			for i in split_value:
				
				more_split_value = i.split('_')[0]
				no_count.append(more_split_value)
			no_count.sort()
			self.df.loc[index, "Genomic_Position"] = [[no_count]]

	def replace_with_grch38_coordinates(self):
		'''
		The current genomic positions are only in grch37 this
		creates a new column in the dataframe with the grch38
		coordinates obtained by the convert_between_builds.py script
		'''
		series = pd.Series(grch38_coordinates)
		self.df['GRCh38_coordinates'] = series


	def add_hgnc_ids_to_df(self):
		gene_name_list = []
		for index, row in self.df.iterrows():
			gene_name_list.append(row['Hugo_Symbol'])

		hgnc_ids = []
		for gene_name in gene_name_list:
			hgnc_id = request_hgnc_id(gene_name)
			hgnc_ids.append(hgnc_id)
		print(gene_name_list)
		hgnc_series = pd.Series(hgnc_ids)
		self.df['HGNC_IDs'] = hgnc_series

			
