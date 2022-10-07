class Estudante:
    escola = 'DIO' #variável de classe

    def __init__(self, nome, matricula):
        self.nome=nome #variável de instância
        self.matricula=matricula #variável de instância

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante('Guilherme', 1)
aluno_2 = Estudante('Giovana', 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola= 'Python' #mudando a variável de classe
aluno_1.matricula = 3 #mudando a variável de instância
aluno_3 = Estudante('Chappie', 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)

