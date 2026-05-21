"""
1.	Crie uma classe Pessoa
Enunciado:
 Crie uma classe Pessoa com nome e idade. Depois crie um objeto e imprima seus dados.

"""

class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fala(self):
        print(f"Meu nome é {self.name} e tenho {self.age} anos de idade")

p = Pessoa("Jorge", 27)
p.fala()
