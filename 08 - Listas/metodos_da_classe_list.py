#append- adiciona valores ao fim da pilha

lista = []

lista.append(2)
lista.append('Python')
lista.append([1,2])
print(lista)

#clear

lista.clear()
print(lista)

#copy
lista = [1,2,3]

l2 = lista.copy()
print(l2)
print(id(lista), id(l2))

#count
lista = ['a', 'b', 'a']

print(lista.count('a'))
print(lista.count('b'))
print(lista.count('c'))

#extend
linguas = ['pt', 'en']
print(linguas)

linguas.extend(['ru', 'es'])
print(linguas)

#index
print(linguas.index('pt')) #0

#pop - remove o último item, passando parêmetro remove o do index passado
print(linguas.pop()) #es
print(linguas) #['pt', 'en', 'ru']
print(linguas.pop(0)) #pt
print(linguas) #['en','ru']

#remove - remove a primeira referência de um valor
lista = ['a', 'b', 'a']
lista.remove('a')

print(lista)

#reverse
lista.reverse() #['b', 'a']
print(lista)

#sort
linguagens = ['python', 'js', 'c','java', 'csharp']
linguagens.sort() #ordena alfabeticamente
print(linguagens)

linguagens.sort(reverse=True)
print(linguagens)

linguagens.sort(key= lambda x: len(x)) #em ordem de tamanho, crescente
print(linguagens)

linguagens.sort(key= lambda x: len(x), reverse=True) #em ordem de tamanho, crescente
print(linguagens)
#caso ambos tenham o mesmo tamanho, o sort coloca primeiro o que aparece primeiro

#funções built-in

#len - vê o tamanho da lista
print(len(linguagens))

#sorted
print(sorted(linguagens, key= lambda x: len(x))) #não altera a lista
print(linguagens)




