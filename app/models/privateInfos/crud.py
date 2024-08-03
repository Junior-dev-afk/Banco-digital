import sqlite3


def get_db_connection():
    c = sqlite3.connect("app/datas/usersInfos.db")
    c.row_factory =sqlite3.Row
    return c

def init_db ():
    c = get_db_connection()
    cursor = c.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS infos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            foto TEXT NOT NULL,
            saldo TEXT NOT NULL,
            pix TEXT NOT NULL
        )
    ''')
    c.commit()
    c.close()

init_db()


class Crud ():
    def __init__(self) -> None:
        pass

    def create(self, user, cpf):
        connect = get_db_connection()
        cursor = connect.cursor()
        cursor.execute('''
            INSERT INTO infos (user, foto, saldo, pix) VALUES (?, ?, ?, ?)
        ''', (user, "static/icons/perfil.png", "0", cpf))
        connect.commit()
        connect.close()

    def read(sel, user):
        connect = get_db_connection()
        cursor = connect.cursor()
        cursor.execute('''
            SELECT * FROM infos WHERE user = ?
        ''', (user,))
        info = cursor.fetchall()
        todos = {}
        for users in info :
            todos = {"user" : users["user"], "foto" : users["foto"], "saldo" : users["saldo"], "pix" : users["pix"]}
        print(todos)
        connect.close()
        return todos

    def update(self, user, item, novo):
        connect = get_db_connection()
        cursor = connect.cursor()
        cursor.execute(f"UPDATE infos SET {item} = ? WHERE user = ?", (novo, user, ))
        connect.commit()
        connect.close()

    def delete(self, user):
        connector = get_db_connection()
        cursor = connector.cursor()
        cursor.execute('''
            DELETE FROM infos WHERE user = ?
        ''', (user,))
        connector.commit()
        connector.close()

    def getUserFromChavePix (self, chave):
        connect = get_db_connection()
        cursor = connect.cursor()
        cursor.execute(f'''
            SELECT * FROM infos WHERE pix = ?
        ''', (chave,))
        all = cursor.fetchall()
        for u in all :
            conta = {"user" : u["user"]}
        connect.close()
        return conta
        

    def isChaveExistAndNotMy(self, chave, user):
        connect = get_db_connection()
        cursor = connect.cursor()
        cursor.execute('''
            SELECT * FROM infos WHERE pix = ?
        ''', (chave,))
        all = cursor.fetchall()
        connect.close()
        if len(all) > 0 :
            if all[0]["user"] != user :
                return True
            return "Você não pode enviar pix para si mesmo"
        return "Essa chava pix não está vinculada a nenhuma conta"


    def haveMoneyInAccount(self, user, valor):
        valor = int(valor)
        connect = get_db_connection()
        cursor = connect.cursor()
        cursor.execute('''
            SELECT * FROM infos WHERE user = ?
        ''', (user,))
        all = cursor.fetchall()
        connect.close()

        if int(all[0]["saldo"]) >= valor :
            return True
        return "Você não tem saldo na conta"
    


crud = Crud()
