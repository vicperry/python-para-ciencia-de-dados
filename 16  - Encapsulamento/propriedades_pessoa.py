class Pessoa:
    def __init__(self,nome, ano_nascimento):
        self.nome = nome 
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa('Barbie', 1996)
print(f'Nome: {pessoa.nome}, Idade: {pessoa.idade}')