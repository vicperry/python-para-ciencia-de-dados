nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ') 
#todo input é convertido em string

print(nome, idade)
print(nome, idade, end= "... \n") #\n quebra a linha, é o valor de end padrão
print(nome, idade, sep="#")