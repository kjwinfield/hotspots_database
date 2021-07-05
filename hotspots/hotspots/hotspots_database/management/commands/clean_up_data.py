
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

    
	def split_by_pipe(self):
		for index, row in self.df.iterrows():
			value = row["Genomic_Position"]
			split_value = value.split('|')
			genome_position_list.append(split_value)
			reps = [len(genome_position_list) for val in self.df.Hugo_Symbol]
			
			# value = row["Genomic_Position"]
			# split_value = value.split('|')
			# genome_position_list.append(split_value)
			self.df.loc[np.repeat(self.df.index.values, reps)]
			# new_df = {'Genomic_Positions_All':  genome_position_list}
			# df2 = pd.DataFrame (new_df, columns = ['Genomic_Positions_All'])
			# return genome_position_list, df2
	
	def remove_mutation_count_from_position(self):
		'''
		Currently the genome positions are stored in the format 4:153250882_3
		where the _3 is the count of samples with a mutation at that position.
		This is very unhelpful so this function strips off the count from the
		genomic position
		'''
		for index, row in self.df.iterrows():
			value = row["Genomic_Position"]
			split_value = value.split('|')
			for i in split_value:
				no_count = []
				more_split_value = value.split('_')
				no_count.append(more_split_value)
			self.df.loc[index, "Genomic_Position"] = [no_count]
