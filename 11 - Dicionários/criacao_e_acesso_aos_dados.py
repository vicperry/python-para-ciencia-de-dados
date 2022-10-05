#Dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário.

pessoa = {'nome': 'Pedro', 'idade': 20}

pessoa = dict(nome='Pedro', idade = 20)

pessoa['telefone'] = '3333-5555' #adicionando uma nova chave:valor a um dicionário já criado

#Acessando valores
pessoa['nome']
pessoa['idade']
pessoa['telefone']

#Sobreescrevendo valor
pessoa['nome'] = 'Maria'

#Dicionários aninhados
contatos = {
    'maria@gmail.com': {'nome': 'Maria', 'telefone': '555-2222'},
    'pedro@gmail.com': {
        'nome': 'Pedro', 'telefone': '555-1111'
    }
}

print(contatos['maria@gmail.com']['nome'])

#Iterar dicionários
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

