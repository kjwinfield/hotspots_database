
import pandas as pd
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta
genome_position_list = []

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
