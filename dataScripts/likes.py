import csv, random

outfile = open('likes.csv', 'wb')
writer = csv.writer(outfile, lineterminator='\n')

with open('beerRating.csv', 'rb') as infile:
	reader = csv.reader(infile)
	for row in reader:
		if row[2]=='4' or row[2]=='5':
			string = row[0], row[1]
			writer.writerow(string)
