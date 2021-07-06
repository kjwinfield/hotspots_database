from django.core.management.base import BaseCommand
from hotspots_database.models import (
									GeneName,
                    				GrCh37,
  					                GrCh38
                    				)
class Command(BaseCommand):
	help = 'Wipes the tables'

	def handle(self, *args, **kwargs):
		""" Wipes the tables of the database completely."""
		answer = None
		while answer not in ("Y", "N"):
			answer = input("Do you want to wipe the db? ").upper()
		if answer == "Y":

			GeneName.objects.all().delete()
			GrCh37.objects.all().delete()
			GrCh38.objects.all().delete()

			print("The tables have now been cleared.")