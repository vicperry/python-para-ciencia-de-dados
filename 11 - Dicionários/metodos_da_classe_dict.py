#clear
pessoas = {
    'pessoa_1': {'nome': 'Ana', 'idade': 20},
    'pessoa_2': {'nome': 'Beto', 'idade': 21}
}

pessoas.clear()
print(pessoas)

#copy
pessoas = {
    'pessoa_1': {'nome': 'Ana', 'idade': 20},
    'pessoa_2': {'nome': 'Beto', 'idade': 21}
}

copia = pessoas.copy()

#fromkeys
outras_pessoas = dict.fromkeys(['pessoa_3', 'pessoa_4'])
outras_pessoas_2 = dict.fromkeys(['pessoa_5', 'pessoa_6'], 'ninguém')
print(outras_pessoas)
print(outras_pessoas_2)

#get
#testando com chaves inexistentes
#pessoas['chave'] #KeyError
pessoas.get('chave') #None
pessoas.get('chave', 'vazio') #vazio
#chave existente
print(pessoas.get('pessoa_1'))

#items - retorna uma lista com cada chave-valor numa tupla
print(pessoas.items()) #pedict_items([('pessoa_1', {'nome': 'Ana', 'idade': 20}), ('pessoa_2', {'nome': 'Beto', 'idade': 21})])

#pop - necessita parâmetro
pessoa_2 = pessoas.pop('pessoa_2')
print(pessoa_2)
print(pessoas)

#popitem - remove o último item inserido no dicionário e torná-lo uma tupla

pessoas = {
    'pessoa_1': {'nome': 'Ana', 'idade': 20},
    'pessoa_2': {'nome': 'Beto', 'idade': 21}
}
pessoa_2 = pessoas.popitem()

print(pessoa_2)
print(pessoas)

#setdefault
#Cria um valor padrão para uma chave que ainda não foi definida
contato = {
  'nome': 'Asa',
  'idade': 10
}

contato.setdefault('telefone', 'vazio')

print(contato)

#update - Passe em dicionário a chave-valor que você deseja atualizar.
contato.update({'nome': 'Alma'})

print(contato)

#values - só valores, sem chaves
print(pessoas.values())

#in
print('pessoa_1' in pessoas) #True
print('pessoa_2' in pessoas) #False

#del

del pessoas['pessoa_1']

print(pessoas) #vazio





