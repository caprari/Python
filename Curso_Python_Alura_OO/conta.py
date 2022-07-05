
# from Curso_Python_Alura_OO.conta import Conta

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo Objeto {self}')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'O saldo do titular {self.titular} é R$ {self.saldo}.')

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor




