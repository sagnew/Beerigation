import MySQLdb

def sqlVoter(beerName):

	db = MySQLdb.connect(host="localhost", user="root", passwd="faBSb04A", db="testDB")
	cursor = db.cursor()
	beers = []
	query ="select b.name from likes l, beer b where l.drinkerID in (select d.id from likes l, drinker d where d.id = l.drinkerID and (select id from beer where     name='" + beerName + "')  = l.beerID) and b.id=l.beerID group by b.name"
	cursor.execute(query);
	db.commit()
	numrows = int(cursor.rowcount)
	for x in range(0,numrows):
		row = cursor.fetchone()
		beers.append(row[0])
	return beers

def sqlManf(beerName):

	db = MySQLdb.connect(host="localhost", user="root", passwd="faBSb04A", db="testDB")

	cursor = db.cursor()
	beers = []
	query="select b.name from beer b where b.manf in (select manf from beer where name='" + beerName + "') group by b.name"
	cursor.execute(query);
	db.commit()
	numrows = int(cursor.rowcount)
	for x in range(0,numrows):
		row = cursor.fetchone()
		beers.append(row[0])
	return beers

def sqlType(beerName):

	db = MySQLdb.connect(host="localhost", user="root", passwd="faBSb04A", db="testDB")

	cursor = db.cursor()
	beers = []
	cursor.execute("select type from beer where name='" + beerName + "'")
	db.commit()
	row = cursor.fetchone()
	if not row[0]:
		return beers
	query="select b.name from beer b where b.type in (select type from beer where name='" + beerName + "') group by b.name;"
	cursor.execute(query);
	db.commit()
	numrows = int(cursor.rowcount)
	for x in range(0,numrows):
		row = cursor.fetchone()
		beers.append(row[0])
	return beers

def sqlCustom(query):

	db = MySQLdb.connect(host="localhost", user="root", passwd="faBSb04A", db="testDB")

	cursor = db.cursor()
	beers = []
	cursor.execute(query)
	db.commit()
	numrows = int(cursor.rowcount)
	for x in range(0,numrows):
		row = cursor.fetchone()
		beers.append(row)
	return beers

sqlCustom("select b.name from beer b where b.type in (select type from beer where name='Zwickelbier') group by b.name;")
