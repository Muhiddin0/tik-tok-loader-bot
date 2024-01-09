
import sqlite3

class Model:

    def __init__(self) -> None:
        self.db = sqlite3.connect('data/data.db')
        self.sql = self.db.cursor()    
        self.sql.execute("CREATE TABLE IF NOT EXISTS users (user_id INT)")

    def addUser(self, user_id):
        self.sql.execute("SELECT * FROM users WHERE user_id = {}".format(user_id))
        if not self.sql.fetchall():
            self.sql.execute("INSERT INTO users VALUES (?)", [user_id])
            self.db.commit()