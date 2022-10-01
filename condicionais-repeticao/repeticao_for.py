#Vale a pena usar for quando se sabe o número de vezes que quer que o comando seja repitido.

texto = input('Escreva um texto: ')
VOGAIS = 'AEIOU'

print('Tirando as consoantes, o texto fica: ')
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end= "")
else:
    print('\nFim de programa')