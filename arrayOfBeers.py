import csv

def arrayOfBeers():
	beer = []
	with open('beer.csv', 'rb') as infile:
		reader = csv.reader(infile)
		for row in reader:
			beer.append(row[1])
	print beer
	return beer
