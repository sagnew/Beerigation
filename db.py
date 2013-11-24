import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="testDB")

cursor = db.cursor()

cursor.execute("SELECT * FROM beer");

db.commit()

numrows = int(cursor.rowcount)

for x in range(0,numrows):
	row = cursor.fetchone()
	print row[0], "-->", row[1], row[2], row[3]
