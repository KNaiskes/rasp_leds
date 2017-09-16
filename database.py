import sqlite3

database = "users.db"

def createDB():
	conn = sqlite3.connect(database)
	db = conn.cursor()
	db.execute("CREATE TABLE IF NOT EXISTS users (name text, password text)")
	conn.commit()
	db.close()

def addUser(name, password):
	if checkUser(name,None) == True:
		print("user : {} already exists".format(name))
	else:
		conn = sqlite3.connect(database)
		db = conn.cursor()
		db.execute("INSERT INTO users VALUES(?,?)",(name,password,))
		conn.commit()
		db.close()


def checkUser(name, password):
	conn = sqlite3.connect(database)
	db = conn.cursor()
	if(password == None):
		db.execute("SELECT * FROM users WHERE name = ?",(name,))
	else:
		db.execute("SELECT * FROM users WHERE name = ? AND password = ?",(name,password,))

	exist = db.fetchone()
	if exist is None:
		return False
	else:
		return True

	db.close()

