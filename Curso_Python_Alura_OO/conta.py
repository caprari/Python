
# from Curso_Python_Alura_OO.conta import Conta

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo Objeto {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'O saldo do titular {self.__titular} é R$ {self.__saldo}.')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('Valor superior ao limite')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @property
    def conta(self):
        return self.__numero

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return {'001 - Banco do Brasil',
                '104 - Caixa',
                '341 - Itaú'}




