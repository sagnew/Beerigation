import csv, random

outfile = open('sells.csv', 'wb')
writer = csv.writer(outfile, lineterminator='\n')

for x in range(0, 200000):
	beer = random.randint(1,5914)
	bar = random.randint(1,10000)
	string = beer, bar
	writer.writerow(string)

