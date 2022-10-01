nome = 'Beto'
idade = 20
profissao = 'médico'

pessoa = {"nome": nome, "idade": idade, "profissao": profissao}

#concatenação
print("Oi, meu nome é " + nome + ", tenho " + str(idade) + " anos e sou " + profissao +".")

#old style
print("Oi, meu nome é %s, tenho %s anos e sou %s." % (nome, idade, profissao))

#format
print("Oi, meu nome é {}, tenho {} anos e sou {}.".format(nome, idade, profissao))

print("Oi, meu nome é {2}, tenho {0} anos e sou {1}.".format(idade, profissao, nome))

print("Oi, meu nome é {name}, tenho {age} anos e sou {job}.".format(name = nome, age = idade, job = profissao))

print("Oi, meu nome é {nome}, tenho {idade} anos e sou {profissao}.".format(**pessoa))

#f
print(f"Oi, meu nome é {nome}, tenho {idade} anos e sou {profissao}.")

#arredondando números com f
PI = 3.14159
print(f'Valor de PI: {PI:.2f}')
print(f'Valor de PI: {PI:10.2f}')

