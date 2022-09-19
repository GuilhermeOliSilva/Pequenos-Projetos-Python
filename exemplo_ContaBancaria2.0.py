class ContaBancaria:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.__saldo = saldo #atributo privado
        global senha #cria uma variável global
        senha = None

    def __repr__(self):
        return (f"Número da conta: {self.numero}\n" +
                f"Titular........: {self.titular}\n" +
                f"Saldo..........: {self.__saldo:.2f}")
    

    @property #propriedade, será visto como um atributo
    def saldo(self):
        global senha
        if senha == None or senha != "123":
            senha = input("Senha: ")
        if senha == "123":
            return self.__saldo
        else:
            senha = None
            return None

    @saldo.setter #setter -> setador, definir
    def saldo(self, valor):
        if valor > 3*self.__saldo:
            print("Atividade suspeita!")
            print("Aumento acima do permitido!")
        elif valor < 0.50*self.__saldo:
            print("Atividade suspeita!")
            print("Redução além do permitido!")
        else:
            self.__saldo = valor

c1 = ContaBancaria(874, "Ana", 7500.00)
print(f"Saldo: R$ {c1.saldo:.2f}")
c1.saldo = 8000.00
print(f"Saldo: R$ {c1.saldo:.2f}")
# c1.set_saldo((c1.get_saldo(senha) + 10*c1.get_saldo(senha)))
# print(f"Saldo: R$ {c1.get_saldo(senha):.2f}")
# c1.set_saldo(1.00)