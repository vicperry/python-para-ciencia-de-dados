class Bicicleta:
    def __init__(self, cor, marca, ano, valor, aro = 18):
        self.cor = cor
        self.marca = marca
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print('Plim! Plim!')

    def parar(self):
        print('Parando...')
        print('Bicicleta parada.')

    def correr(self):
        print('Vrummm...')

    #def __str__(self):
    #    return f'Bibicleta: {self.cor},{self.marca},{self.ano},{self.valor}'

    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"


b1 = Bicicleta('vermelha', 'caloi', 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.marca, b1.ano, b1.valor)

b2 = Bicicleta('verde','monark',2000,190)
Bicicleta.buzinar(b2)

print(b2)

