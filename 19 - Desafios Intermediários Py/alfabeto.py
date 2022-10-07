#Desafio
#Dada a letra N do alfabeto, nos diga qual a sua posição.
#
#Entrada
#Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).
#
#Saída
#Um único inteiro, que representa a posição da letra no alfabeto.
letra = input()

abc = []
for n in range(ord('a'), ord('z')+1):
    abc.append(chr(n).upper())

for n in abc:
    if letra == n:
        print(abc.index(n) + 1)
        break
