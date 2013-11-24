import csv

outfile = open('beer.csv', 'wb')
writer = csv.writer(outfile,delimiter=',', lineterminator='\n');
brewies = {}
with open('breweries.csv') as brew:
	reader = csv.reader(brew)
	i = 0
	for row in reader:
		if i!=0:
			brewies[row[0]] = row[1]
		i+=1
print brewies

brew.close()

types = {}
with open('styles.csv', 'rb') as style:
	reader = csv.reader(style)
	i = 0
	for row in reader:
		if i!=0:
			types[row[0]] = row[2]
		i+=1
print types

with open('beers.csv', 'rb') as infile:
	reader = csv.reader(infile,delimiter=',', lineterminator='\n')
	rownum = 0
	for row in reader:
		if rownum==0:
			rownum+=1
			continue
		if row[4]=='-1':
			tp = ""
		else:
			tp = types[row[4]]
		if row[1]==-1:
			manf = ""
		else:
			manf = brewies[row[1]]
		string = row[0],row[2], manf, tp
		writer.writerow(string)
