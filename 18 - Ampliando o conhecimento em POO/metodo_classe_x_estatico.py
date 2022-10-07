class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod #método de classe cria classes usando outros parâmetros
    def criar_de_data_nascimento(cls,ano,mes,dia,nome):
        idade = 2022 - ano 
        return cls(nome,idade)

    #método estático
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

#p = Pessoa('Lana', 30)
#print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(1994,3,21,'Paula')
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(16))