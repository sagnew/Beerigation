import csv

outfile = open('drinker.csv', 'wb')
writer = csv.writer(outfile, lineterminator='\n')

with open('names.csv', 'rb') as infile:
	reader = csv.reader(infile)
	for row in reader:
		name = row[1] + " " + row[2]
		address = row[3] + " " + row[4]
		string = row[0], name, address, row[5]
		writer.writerow(string)
