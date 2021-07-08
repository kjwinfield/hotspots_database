from configparser import RawConfigParser

def write_data_to_file(cleaned_data):
	"""Insert data into the database"""
	config = RawConfigParser()
	config.read('../credentials.ini')

	f = open("grch37_coordinates.bed", "w")
	# Loop through each row and write to file in the bed format
	for index, row in cleaned_data.df.iterrows():
		f.write(
				'chr' + row["Genomic_Position"][0][0].split(':')[0]
				+ '\t' + row["Genomic_Position"][0][0].split(':')[1]
				+ '\t' + row["Genomic_Position"][0][-1].split(':')[1]
				+ '\n')
	f.close()
