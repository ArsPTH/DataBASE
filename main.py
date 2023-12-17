import sqlite3

base = sqlite3.connect('new.db')
cur = base.cursor()


base.execute('CREATE TABLE IF NOT EXISTS {}(login PRIMARY KEY, password)'.format('data'))
base.commit()
"""
cur.execute('INSERT INTO data VALUES(?, ?)', ('jonny123', '123456789'))
base.commit()
cur.execute('INSERT INTO data VALUES(?, ?)', ('billy123', 'password'))
base.commit()
r = cur.execute('SELECT password FROM data').fetchall()
print(r)
r = cur.execute('SELECT password FROM data WHERE login == ?', ('jonny123',)).fetchone()
print(r)
"""

cur.execute('INSERT INTO data VALUES(?, ?)', ('jonny123', '123456789'))
base.commit()
cur.execute('INSERT INTO data VALUES(?, ?)', ('billy123', 'password'))
base.commit()

#cur.execute('DELETE FROM data WHERE password == ?',('123456789',))
#base.commit()
#base.execute('DROP TABLE IF EXISTS data')
#base.commit()