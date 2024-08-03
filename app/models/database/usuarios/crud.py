import sqlite3
from app.models.database.crypt import criptografar
from app.models.privateInfos.crud import crud


def get_db_connection():
    conn = sqlite3.connect("app/datas/usuarios.db")
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            user TEXT NOT NULL,
            cpf TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

initialize_database()

class Crud ():

    def __init__(self):
        pass


    def create (self, email, user, cpf, password):
        connector = get_db_connection()
        cursor = connector.cursor()
        cursor.execute('''
            INSERT INTO users (email, user, cpf, password) VALUES (?, ?, ?, ?)
        ''', (email, user, cpf, criptografar.cryp.encrypt(password)))
        crud.create(user, cpf)
        connector.commit()
        connector.close()

    def read (self):
        connector = get_db_connection()
        cursor = connector.cursor()
        cursor.execute("SELECT * FROM users")

        all = cursor.fetchall()
        allUsers = []
        for user in all :
            obj = {"user" : user["user"], "email" : user["email"], "cpf" : user["cpf"], "password" : criptografar.cryp.decrypt(user["password"])}
            allUsers.append(obj)
        connector.close()
        return allUsers

    def readFromUser (self, user):
        todos = self.read()
        for users in todos:
            if users["user"] == user:
                return users
        return False

    def update(self):
        pass

    def delete(self, user):
        connector = get_db_connection()
        cursor = connector.cursor()
        cursor.execute('''
            DELETE FROM users WHERE user = ?
        ''', (user,))
        crud.delete(user)
        connector.commit()
        connector.close()

database = Crud()

