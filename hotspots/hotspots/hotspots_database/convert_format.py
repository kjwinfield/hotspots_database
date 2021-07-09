'''
Quick throwaway script to convert the TERT hotspots from
the excel file provided in the user requirements meeting to
match the hotspots_v2.xls file that will be used to seed 
the database
'''	
    
f = open("unconverted.bed", "r")
nf = open("converted.bed", "w")
# Loop through each row and write to new file in the bed format
for row in f:
    nf.write(row.split('\t')[0].strip('chr')
            + ':' + row.split('\t')[1] + '_3|'
            + row.split('\t')[0].strip('chr')
            + ':' + row.split('\t')[2].strip('\n') + '_3' + '\n')
f.close()
nf.close()