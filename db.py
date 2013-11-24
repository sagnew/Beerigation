import MySQLdb

def sqlCreator(beerName, searchby):

	db = MySQLdb.connect(host="localhost", user="root", passwd="", db="testDB")

	cursor = db.cursor()

	if searchby == 0:
		query ="select b.name from likes l, beer b where l.drinkerID in (select d.id from likes l, drinker d where d.id = l.drinkerID and (select id from beer where     name='" + beerName + "')  = l.beerID) and b.id=l.beerID group by b.name"
		print query
		cursor.execute(query);
		db.commit()
		numrows = int(cursor.rowcount)
	for x in range(0,numrows):
		row = cursor.fetchone()
		print row[0]

sqlCreator("Zwickelbier", 0)
