#Herança é a capacidade da classe filha de derivar métodos da classe mãe.
#Ela permite representar melhor os relacionamentos do mundo real, a reutilização de código.
#É de natureza transitiva, passando de pai para filho, filho para neto.

#Herança simples:
class A:
    pass

class B(A): #classe B extende de classe A // B é filha da classe A
    pass

#Herança múltipla
class A:
    pass

class B:
    pass

class C(A,B):
    pass

