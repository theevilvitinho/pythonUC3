# Criando a base (planta do objeto)
class Carro:
    def __init__(self,motor,quant_rodas):
        self.motor = motor
        self.quant_rodas = quant_rodas

    """def __init__(self):
        pass"""

    def deslocar(self):
        print("Carro está andando")


# Sem valores obrigatórios
class Conta:
    def __init__(self):
        pass


class Funcionario:
    nome = ""
    idade = 0
    cargo = ""


# Criando o objeto
car1 = Carro("V8",4)
car2 = Carro("V6",4)
"""car3 = Carro()
car3.motor = "V12"  # Atribuindo o valor à propriedade do objeto
print(car3.motor)
car3.deslocar() # Executando a função (ação) do objeto"""



# Mostrar informações do objeto
print(f"Carro 1 tem o motor: {car1.motor}")
print(f"Carro 2 tem o motor: {car2.motor}")

class Cliente:
    def __init__(self,nome,cpf,telefone,email):
        self.nome = nome
        self.cpf = cpf
        self.telefone =telefone
        self.email = email

cli1 = Cliente(nome="Sérgio",cpf="123.456.789-07",telefone="(21)98374-8374",email="sergiodoispontos@gmail.com")
cli2 = Cliente(nome="jorge",cpf="-98.765.432-01",telefone="(21)95546-3743",email="jorgedopneu@gmail.com")

print(f"\nNome do cliente: {cli1.nome}\nCPF: {cli1.cpf}\nTelefone: {cli1.telefone}\nE-mail: {cli1.email}")


class Ovo:
    def cozinhar(self):
        print("Ovo está cozinhando")

    def fritar(self):
        print("Ovo está fritando")

ovo = Ovo()
ovo.cozinhar()
ovo.fritar()


class Aluno:
    def estudar(self):
        for i in range(5):
            print("Estou estudando")

    def vouEstudar(self,resposta):
        if resposta == "sim":
            print("Bons estudos")
        else:
            print("Acho que é melhor você estudar")

aluno = Aluno()
aluno.estudar()

resposta = input("Você vai estudar hoje?")
aluno.vouEstudar(resposta)