import csv

adjs = {}
nouns = {}
with open('adjectives.txt', 'rb') as adjfile:
	content = adjfile.readlines()
i = 0
for x in content:
	adjs[i]=x.rstrip()
	i+=1
print adjs
with open('noun.txt', 'rb') as nounfile:
	content = nounfile.readlines()
i = 0
for x in content:
	nouns[i]=x.rstrip()
	i+=1
print nouns

outfile = open('bars.csv', 'wb')
writer = csv.writer(outfile, lineterminator='\n')

with open('barInfo.csv', 'rb') as infile:
	reader = csv.reader(infile)
	a = 0
	n = 0
	for row in reader:
		if n==100:
			a+=1
			n=0
		name = adjs[a] + " " + nouns[n]
		place = row[1] + " " + row[2]
		string = row[0], name, place, row[3]
		print string
		writer.writerow(string)
		n+=1
