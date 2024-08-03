from app.models.privateInfos.crud import crud


class Saldo ():

    def __init__(self):
        pass


    def add (self, user, valor):
        valor = int(valor)
        saldo =  int(crud.read(user)["saldo"])
        valor = saldo + valor
        valor = str(valor)
        crud.update(user, "saldo", valor)

    def remove(self, user, valor):
        valor = int(valor)
        saldo =  int(crud.read(user)["saldo"])
        if saldo >= valor:
            valor = saldo - valor
            valor = str(valor)
            crud.update(user, "saldo", valor)


saldo = Saldo()