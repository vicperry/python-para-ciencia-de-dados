#while é usado quando não se sabe ao certo o número de vezes que queremos repetir um comando.
print('Qual é o número do Cristiano Ronaldo?')

while True:
    numero = int(input("Digite um número: "))

    if numero == 7:
        print('Esse é o número!')
        break
    
    print(f'Não é {numero}!')

print('Cristiano Ronaldo é 7!')