#Interfaces definem o que uma classe deve fazer e não como. Para construir uma interface em Python, cria-se uma classe abstrata que vai sar herança para uma classe filha. Assim se aplica um contrato de interface no Python.

from abc import ABC,abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando TV...\nLigada.')

    def desligar(self):
        print('Desligando TV...\nDesligada.')

    @property
    def marca(self):
        return 'LG'

controle = ControleTV()

controle.ligar()
controle.desligar()
print(controle.marca)

