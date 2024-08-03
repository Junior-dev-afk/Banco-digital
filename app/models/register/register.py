import re
from app.models.database.usuarios.crud import database
from .verifyCpf import verifyCpf

class Register ():

    def __init__(self) :
        pass


    # verificar email

    def emailIsReal (self, email):
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
        if re.match(padrao, email):
            return True
        else:
            return False
        

    def emailUsed(self, email):
        for user in database.read():
            if user["email"] == email:
                return True
        return False

    def verifyEmail (self, email):
        if self.emailIsReal(email):
            if not self.emailUsed(email) :
                return True
            return "Este email ja foi cadastrado"
        return "Digite um email real"

    #ferifica usuario

    def userUsed (self, username):
        for user in database.read():
            if user["user"] == username:
                return True
        return False
    
    #verifica cpf

    def cpfIsReal(self, cpf):
        return verifyCpf.cpfIsReal(cpf)
            

    def cpfIsUsed(self, cpf):
        for user in database.read():
            if user["cpf"] == cpf:
                return True
        return False
    
    def verifyCpf(self, cpf):
        if self.cpfIsReal(cpf) :
            if not self.cpfIsUsed(cpf) :
                return True
            return "Esse cpf já foi cadastrado"
        return "Esse cpf não é real"

    
    #verifica senha

    def passwordStrong(self, password):
        if len(password) >= 8 :
            return True
        return False

    def passwordCompatible(self, pass1, pass2):
        return pass1 == pass2
    
    def verifyPassword(self, pass1, pass2):
        if self.passwordStrong(pass1):
            if self.passwordCompatible(pass1, pass2):
                return True
            return "As senhas nao coincidem"
        return "Sua senha deve ter ao menos 8 digitos"



    def register (self, email, usuario, cpf, pass1, pass2):
        if not all([email, usuario, cpf, pass1, pass2]):
            return "Preencha todos os campos"

        if self.verifyEmail(email) != True :
            return self.verifyEmail(email)
        

        if self.userUsed(usuario):
            return "Usuário já está sendo usado"
        
       
        if self.verifyCpf(cpf) != True:
            return self.verifyCpf(cpf)
        
        if self.verifyPassword(pass1, pass2) != True:
            return self.verifyPassword(pass1, pass2)

        database.create(email, usuario, cpf, pass1)
        return True


register = Register()