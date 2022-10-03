print('São números ímpares: ')

for numero in range(0, 11):
    
    if numero % 2 == 0:
        continue
    print(numero, end=" ")

else:
    print()