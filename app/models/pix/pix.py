from app.models.privateInfos.crud import crud
from app.models.saldo.saldo import saldo
from app.models.database.usuarios.crud import database


class Pix ():

    def __init__(self):
        pass
        

    def enviar (self, pagador, senha, chave, valor ):
        valor = int(valor)
        if valor > 0 :
            data = crud.getUserFromChavePix(chave)
            user = database.readFromUser(pagador)
            saldo_user = crud.read(user["user"])["saldo"]
            if user["password"] == senha:
                if int(saldo_user) >= valor and data["user"] :
                    recebedor = data["user"]
                    saldo.remove(pagador, valor)
                    saldo.add(recebedor, valor)
                    return True
                return "Saldo insuficiente"
            return "Senha não corresponde"
        return "O valor nao pode ser menor ou igual a 0"
    
pix = Pix()