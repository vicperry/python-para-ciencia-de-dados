#Encapsulamento é a proteção dos atribtos ou métodos de uma classe. Existem o public e private (definido por _ antes do nome). Trata-se de uma convenção, o interpretador não vai te proibir de acessar algo privado.

class Conta:
    def __init__(self, saldo = 0):
        self.saldo = saldo

    def depositar(self, valor):
        pass

    def sacar(self, valor):
        pass

conta = Conta