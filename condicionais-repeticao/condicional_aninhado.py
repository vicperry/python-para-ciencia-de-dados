idade = int(input('Qual a sua idade? '))

if idade >= 18:
    habilitacao = input("Você tem habilitação? Responda com 'S' ou 'N' ")
    if habilitacao == 'S':
        print('Você pode dirigir.')
    else:
        print('Você não pode dirigir.')
else:
    print('Você não pode dirigir.')

