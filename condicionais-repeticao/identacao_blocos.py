def sacar(valor):
    saldo = 500

    if saldo >= valor:
       print('Valor sacado')
       print('Retire o seu dinheiro na boca do caixa.')

    print('Obrigado por ser nosso clinte')

sacar(300)

#def depositar(valor):
#saldo = 200
#saldo += valor
#Não funciona, pois o Python obriga a identação.

def depositar(valor):
    saldo = 200
    saldo += valor

    print('Novo saldo após deposito: ', saldo)

depositar(100)
