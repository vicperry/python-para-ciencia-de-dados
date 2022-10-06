class Cachorro:
    def __init__(self, nome, cor, acoradado = True):
        print('Inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acoradado

    def __del__(self):
        print('Removendo a instância da classe.')

    def falar(self):
        print('auau')

c = Cachorro('Toto', 'preto')
c.falar()
