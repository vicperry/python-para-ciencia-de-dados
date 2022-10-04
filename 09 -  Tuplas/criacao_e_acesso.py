#tuplas são imutáveis
#declarando

frutas = ('uva', 'maca', 'pera',)

letras = tuple('python')

numeros = tuple([1,2,3])

pais = ('Brasil',)

print(frutas, letras, numeros, pais)

print(pais[0]) #acessando elemento por index

print(frutas[-1])

#aninhando

matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7,8,9),
)

#fatiamento
#tupla[start:stop:step]

#iterar

for fruta in frutas:
    print(fruta)

for indice, fruta in enumerate(frutas):
    print(f'{indice}:{fruta}')


