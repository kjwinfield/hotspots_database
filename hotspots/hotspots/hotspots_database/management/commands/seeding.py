import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import os
import django
from django.core.management.base import BaseCommand
import hotspots_database.management.commands.insert as inserter
import hotspots_database.management.commands.clean_up_data as clean_data

class Command(BaseCommand):
	help = "Seed the database"

	def add_arguments(self, parser):
		parser.add_argument("-d", "--data_path",
							help = 'The path to the data',
							nargs = 1)
	
	def clean_data(self, data_path):
		data = clean_data.Data(data_path)
		data.read_data_into_df(data_path)
		data.remove_mutation_count_from_position_and_sort()

		return data

	def handle(self, *args, **kwargs):
			# Create a list containing samples in the given path
			if kwargs['data_path']:
				data_path = kwargs['data_path']
				# Clean the data
				cleaned_data_df = self.clean_data(data_path[0])
				# Insert the data
				inserter.insert_data(cleaned_data_df)