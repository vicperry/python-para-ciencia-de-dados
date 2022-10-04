#criando listas
frutas = ['laranja', 'banana', 'morango'] #cria conjunto
print(frutas)

frutas = [] #torn[a-o vazio]
print(frutas)

letras = list('python') #cada letra da palavra se torna um elemento com o método list
print(letras)

numeros = list(range(10))
print(numeros)

carro = ['Ferrari', 'F8', 420000, 2020, 2900, 'São Paulo'] #listas comportam dados de diferentes tipos

#acessando itens

frutas = ['uva', 'pera', 'maca']

print(frutas[0]) #uva
print(frutas[-1]) #indice negativo acessa a partir do último item da lista - maca

#listas aninhadas

matriz = [
    [1, 'a', 2],
    ['b', 3, 'dado'],
    [6, 9, 'c']
]

matriz[0] #[1, 'a', 2]
matriz[0][0] #1

#fatiamento
lista = ['p','y','t','h','o','n']
#list[start:end:step]
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

#iteração de lista
carros = ['gol', 'celta', 'palio']

for carro in carros:
    print(carro)

#usa a função enumerate caso seja preciso saber o indice do objeto no laço for
for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

#compreensão de listas
numeros = [1, 30, 21, 8, 2, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)
