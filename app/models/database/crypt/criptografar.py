class Cryp():

    def __init__(self):
        pass

    #adicionar criptografia
    
    def encrypt(self, password):
        encrypted = ""
        for digito in password:
            if digito.isalpha() and len(digito) == 1 :
                encrypted = encrypted + digito
            else:
                encrypted = encrypted + digito
        return encrypted 

    def decrypt(self, password):
        decrypted = ""
        for digito in password:
            if digito.isalpha() and len(digito) == 1 :
                decrypted = decrypted + digito
            else:
                decrypted = decrypted + digito 
        return decrypted 


cryp = Cryp()