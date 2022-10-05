#Função é um bloco de código identificado por um nome que pode receber parâmetros e pode dar um retorno.
#Programar baseado em funções é programação no paradigma estruturada.

def exibir_mensagem(nome):
    print('Olá, mundo! Me chamo', nome,'.')

exibir_mensagem('Vic')

def exibir_mensagem_2(nome= 'Padrão'):
    print('Olá, mundo! Me chamo', nome,'.')

exibir_mensagem_2()
exibir_mensagem_2('Vic')
exibir_mensagem_2(nome='Vyc')

#Retorno da função
#Quando não há um retorno explícito, a funçaõ retorna None.

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([1,2,3]))
print(retorna_antecessor_e_sucessor(5))

#Argumentos nomeados

def salvar_carro(marca, modelo, ano):
    print(f'Carro salvo: {marca}, {modelo}, {ano}')

salvar_carro('fiat','uno',1999)
salvar_carro(marca= 'vw', modelo= 'fusca', ano= 1980)
salvar_carro(**{'marca': 'chevrolet', 'modelo':'corsa','ano':1989}) #valores passados em kwargs

#Args e kwargs
#Args = parâmetro passado com 1 asterístico em forma de tupla
#Kwargs = a mesma coisa, só que com dicionário

def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}'for chave, valor in kwargs.items()])
    print(texto, meta_dados)
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema('Quarta-feira, 5 de outubro', 'No meio do caminho tinha uma pedra', 'Tinha uma pedra no meio do caminho', 'Tinha uma pedra', 'No meio do caminho tinha uma pedra', autor='Carlos Drummond de Andrade', ano='1967')

#Parâmetros especiais
#Positional only - tudo que for antes da barra precisa ser declarado por posição, e tudo que for declarado depois da barra precisa seguir uma única forma de declaração, podendo ser ou por posição ou por palavra-chave

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Palio', 1999, 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina') #válido

#criar_carro(modelo='Palio', ano=1999, placa='ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina') - inválido

#Keyword only - tudo após o * precisa ser declarado por keyword

def criar_carro_1(modelo, ano, placa, *, marca, motor,combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_1('Palio', 1999, 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')

#keyword and positional only - tudo antes da barra é por posição e aṕos *, palavra-chave.

def criar_carro_1(modelo, ano, /, placa, *, marca, motor,combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_1('Palio', 1999, placa= 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')

#Objetos de primeira classe
#Em Python, tudo é objeto, assim como as funções. Com isso, podemos atribuir funções a variáveis, passá-las como parâmetro, usá-las como valores em estruturas de dados e como valor de retorno para uma função(closure).

def somar(a,b):
    return a + b

def exibir_total(a, b, funcao):
    resultado = funcao(a,b)
    print(f'O resultado da operação {a} + {b} = {resultado}')

exibir_total(10,5,somar)

#Escopo local e global
#Alterações feitas no bloco de uma função = local, alterações nela feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado
#Alterações feitas no bloco fora de uma função = global

salario = 2000 #global

def salario_bonus_global(bonus):
    global salario #a palavra-chave 'global' informa para o interpretador que a variável executada pelo interpretador é a global.
    salario += bonus
    return salario

salario_bonus_global(5000)
print(salario)

