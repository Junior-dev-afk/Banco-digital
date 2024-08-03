from app.models.database.usuarios.crud import database 


class Login ():

    def __init__(self):
        pass


    def verifyPassword (self, user, password):
        for users in database.read():
            if users["user"] == user and users["password"] == password:
                return True
        return False



    def login (self, user, password):

        if not self.verifyPassword(user, password):
            return False
            
        return True
    

login = Login()