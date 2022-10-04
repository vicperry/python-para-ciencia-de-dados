#Coleção de objetos com elementos únicos.

set([1,2,3,1,3,2,4]) #{1,2,3,4}

print(set('abacaxi'))

letras = {'a', 'b', 'c','b'}

print(letras)

#Conjuntos em Python não suportam indexação. Precisa converter em lista.

letras = list(letras)
print(letras)
print(letras[1])

#Assim como na matemática:

#union

conj_a = {1,2}
conj_b = {3,4}

print(conj_a.union(conj_b))

#intersection

conj_a = {1,2,3}
conj_b = {3,4,5}

print(conj_a.intersection(conj_b))

#difference

conj_a = {1,2,3}
conj_b = {3,4,5}

print(conj_a.difference(conj_b))

#symmetric_difference
conj_a = {1,2,3}
conj_b = {3,4,5}

print(conj_a.symmetric_difference(conj_b)) #todos os elementos que não estão na interseção

#issubset

conj_a = {1,2,3}
conj_b = {1}

print(conj_a.issubset(conj_b)) #false
print(conj_b.issubset(conj_a)) #true

#isdisjoint

conj_a = {1,2,3}
conj_b = {1}
conj_c = {0}

print(conj_a.isdisjoint(conj_b)) #false
print(conj_a.isdisjoint(conj_c)) #true

#outros métodos

#add
sorteio = {1,2}
sorteio.add(3)
print(sorteio)

#clear
sorteio.clear()
print(sorteio)

#copy
s1 = sorteio.copy()

#discard
sorteio = {1,2,3,4}
sorteio.discard(1)
print(sorteio)

#pop
print(sorteio.pop()) #tira elemento do começo
print(sorteio)

#remove
sorteio.remove(4)
print(sorteio)

#no remove, se o elemento não existir, exibe-se um erro no console. no discard, não.

#len
print(len(sorteio))

#in
numeros = {1,2}

print(1 in numeros)
print(0 in numeros)






