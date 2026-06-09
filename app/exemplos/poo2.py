class Teclado:
    def __init__(self,marca,preco,cor):
        self.marca = marca
        self.preco = preco
        self.cor = cor

    def __str__(self):
        return f"\nMarca: {self.marca}\nPreço: {self.preco}\nCor: {self.cor}"

tecladoMancer = Teclado("Mancer", 250.00, "Preto")
print(tecladoMancer)
tecladoMachenike = Teclado("Machenike", 350.00, "Azul")
print(tecladoMachenike)




# Herança

class Animal:
    def __init__(self,revestimento_externo):
        self.revestimento_externo = revestimento_externo

    def __str__(self):
        return f"\nTipo de revestimento externo: {self.revestimento_externo}"

class Carnivoro(Animal):
    def comer(self):
        print("Está comendo carne")

class Mamifero(Animal):
    def comer(self):
        print("Está mamando")


zebra = Mamifero("Pelo")
print(zebra.comer())



# Polimorfismo

class Passaro:
    def voar(self):
        return "Voando alto"
    
class Aviao:
    def voar(self):
        return "Avião em velocidade de cruzeiro"



def decola(obj):
    print(obj.voar())

decola(Passaro())
decola(Aviao())
