import pandas
import random
import re
import datetime
from django.db import models
#from django.contrib.auth.models import User
# from hotspots_database.models import (
# 											Codon,
# 											AminoAcidChange,
# 											Hotspots,
# 											Gene,
# 											Sample,)
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

		# Insert patient information
		gene, created = Gene.objects.get_or_create(
				first_name = first_name,
				last_name = last_name,
				gene_name = row["Hugo_Symbol"],
				proband = row["Proband"],
                codon_position_id = len(set(row['Amino_Acid_Position']))
                #amino_acid_position = row['Amino_Acid_Position']
                #trinucleotides = row['Codon_Change'].split('|')
				)

		# # Insert sample type information
		# sample_type, created = SampleType.objects.get_or_create(
		# 		sample_type = "Unknown",)

		# # Insert somatic information
		# somatic_information, created = SomaticInformation.objects.get_or_create(
		# 		stage = row["Stage"],
		# 		description = row["Description"])

		# # Insert sample information
		# random_sample_name = random.randint(0,1000000000)
		# sample, created = Sample.objects.get_or_create(
		# 		patient_id = patient,
		# 		sample_name = random_sample_name,
		# 		sample_type = sample_type,
		# 		workflow = -1,
		# 		somatic_information = somatic_information)

		# # Insert sequencer information
		# sequencer, created = Sequencer.objects.get_or_create(
		# 		name = row["Sequencer"],)	

		# # Insert analysis information
		# analysis, created = Analysis.objects.get_or_create(
		# 		sample_id = sample,
		# 		sequencer = sequencer,
		# 		date_sequenced = datetime.datetime.now(),
		# 		runfolder = "Unknown",
		# 		capture = 1)


		# # Insert variant information
		# pos = row["Variant Genome"].replace("(","").replace(")","")
		# pos = pos.split(".")[1]
		# if pos[0] == "?":
		# 	pos = pos.split("_")[1]
		# position = re.findall(r"([0-9]*)",pos)[0]

		# if ">" in pos:
		# 	ref = pos.split(">")[0][-1]
		# 	alt = pos.split(">")[1][0]
		# else:
		# 	ref = "?"
		# 	alt = "?"
		# variant, created = Variant.objects.get_or_create(
		# 		chrom = 17,
		# 		pos = position,
		# 		ref = ref,
		# 		alt = alt,
		# 		raw_g = row["Variant Genome"],
		# 		raw_c = row["Variant cDNA"],
		# 		raw_p = row["Variant Protein"])

		# # Insert RefGenome information
		# refgenome, created = RefGenome.objects.get_or_create(
		# 		name = "?",)		

		# analysisvariant, created = AnalysisVariant.objects.get_or_create(
		# 		variant_id = variant,
		# 		analysis_id = analysis,
		# 		depth = 0,
		# 		genome_id = refgenome)

		# interpretation, created = Interpretation.objects.get_or_create(
		# 		analysis_variant_id = analysisvariant,
		# 		date_analysed = datetime.datetime.now(),
		# 		analysed_by = user,
		# 		pathogenicity = row["Pathogenicity Code"],
		# 		active = True,)

		# for criteria_code in row["Evidence Codes"].split(","):
		# 	criteria, created = Criteria.objects.get_or_create(
		# 			criteria_code = criteria_code,
		# 			description = "test description",
		# 			)

		# 	interpretationcriteria, created = InterpretationCriteria.objects.get_or_create(
		# 			criteria_id = criteria,
		# 			interpretation_id = interpretation,
		# 			)
