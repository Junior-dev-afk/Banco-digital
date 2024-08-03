class Cpf ():

    def __init__(self) :
        pass

    def calcular_digito(self, digitos, pesos):
        soma = sum(int(d) * p for d, p in zip(digitos, pesos))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)
    
    def cpfIsReal(self, cpf):
        cpf = str(cpf) 
        if len(cpf) != 11 or cpf.isdigit() == False:
            return False

        pesos1 = range(10, 1, -1)  
        pesos2 = range(11, 1, -1)  

        primeiro_digito = self.calcular_digito(cpf[:9], pesos1)
        segundo_digito = self.calcular_digito(cpf[:9] + primeiro_digito, pesos2)
        
        return cpf[-2:] == (primeiro_digito + segundo_digito)


verifyCpf = Cpf()