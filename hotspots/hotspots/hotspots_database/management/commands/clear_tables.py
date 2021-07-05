from django.core.management.base import BaseCommand
from hotspots_database.models import (
											Codon,
											
											Hotspots,
											Gene,
											
                                            AllGenomicPositions,)

class Command(BaseCommand):
	help = 'Wipes the tables'

	def handle(self, *args, **kwargs):
		""" Wipes the tables of the database completely."""
		answer = None
		while answer not in ("Y", "N"):
			answer = input("Do you want to wipe the db? ").upper()
		if answer == "Y":

			AllGenomicPositions.objects.all().delete()
			Hotspots.objects.all().delete()

			print("The tables have now been cleared.")