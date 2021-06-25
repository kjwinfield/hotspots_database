
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

class Data:
	def __init__(self, data_path):
		self.read_data_into_df(data_path)

	def read_data_into_df(self, path):
		data_df = pd.read_excel(path)
		self.df = data_df