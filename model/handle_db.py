import sqlite3
from werkzeug.security import generate_password_hash

class HandleDB():
    def __init__(self):
        self._con = sqlite3.connect("./users.sqlite")
        self._cur = self._con.cursor()
    
    def get_all(self):
        data = self._cur.execute("SELECT * FROM users")
        return self._cur.fetchall()
    
    def get_only(self, data_user):
        data = self._cur.execute("SELECT * FROM users WHERE username = '{}'".format(data_user))
        return self._cur.fetchone()

    def get_only_id(self, data_user):
        data = self._cur.execute("SELECT * FROM users WHERE id = '{}'".format(data_user))
        return self._cur.fetchone()

    def insert(self, data_user):
        self._cur.execute("INSERT INTO users VALUES ('{}', '{}', '{}', '{}', '{}')".format(
            data_user['id'],
            data_user['firstname'],
            data_user['lastname'],
            data_user['username'],
            data_user['password_user']
        ))
        self._con.commit()

    def delete_user_by_id(self, user_id):
        query = f"DELETE FROM users WHERE id = '{user_id}'"
        self._cur.execute(query)
        self._con.commit()

    def update_password_for_user(self, user_id, new_password):
        # Encriptar la nueva contraseña
        encrypted_password = generate_password_hash(new_password, "pbkdf2:sha256:30", 30)
        query = f"UPDATE users SET password_user = ? WHERE id = ?"
        self._cur.execute(query, (encrypted_password, user_id))
        self._con.commit()

    def __del__(self):
        self._con.close()
