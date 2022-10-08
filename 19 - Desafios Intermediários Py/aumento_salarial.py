# A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:

# Salário	Percentual de Reajuste
# 0 - 600.00
# 600.01 - 900.00
# 900.01 - 1500.00
# 1500.01 - 2000.00
# Acima de 2000.00

# 17%
# 13%
# 12%
# 10%
# 5%

# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

# A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.

# Exemplo 1
#
#Entrada	Saída
#1000	Novo salario: 1120,00 
#Reajuste ganho: 120,00                                                                                  #   
#Em percentual: 12 %

salario = int(input()) 
reajuste_percento = 0 
novo_salario = 0
reajuste_ganho = 0



if salario <=600:
    reajuste_percento = 17

elif salario > 600 and salario <= 900:
    reajuste_percento = 13

elif salario > 900 and salario <= 1500:
    reajuste_percento = 12

elif salario > 1500 and salario <= 2000:
    reajuste_percento = 10 

else:
    reajuste_percento = 5 
    
reajuste_ganho = salario * reajuste_percento / 100
novo_salario = salario + reajuste_ganho

reajuste_ganho = "{:.2f}".format(reajuste_ganho)
novo_salario = "{:.2f}".format(novo_salario)
reajuste_percento = f"{reajuste_percento} %"

reajuste_ganho = f"{reajuste_ganho}"#.replace('.',',')
novo_salario = f"{novo_salario}"#.replace('.',',')

    
print(f'Novo salario: {novo_salario}\nReajuste ganho: {reajuste_ganho}\nEm percentual: {reajuste_percento}')