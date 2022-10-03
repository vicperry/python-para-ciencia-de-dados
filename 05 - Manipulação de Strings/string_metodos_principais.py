nome = "ThoR"

print(nome)
print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   Olá, mundo   "

print(texto)
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

print(nome.center(10))
print(nome.center(10, "#"))
print("-".join(nome))

print(texto.count('mundo')) #conta quantas vezes o parâmetro surge na variável
print(texto.replace('Olá', 'Tchau')) 
