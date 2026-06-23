# função de soma
def soma(num1,num2):
    total = num1 + num2
    return total

def exibirmsg():
    print("Isso é uma função!")

def exibirmsg2():
    return "Isso é uma função 2!"

print(soma(5,15))

exibirmsg() # com print
print(exibirmsg2())  # com return


# função de subtração
def sub(num1,num2):
    total = num1 - num2
    return total

print(sub(6,1))


# função de multiplicação
def sub(num1,num2):
    total = num1 * num2
    return total

print(sub(5,5,))


# função senha
def test(senha):
    if senha == "12345":
        print("Senha correta!")
    else:
        print("Senha incorreta!")

test(input("Digite a senha: "))


# funcao contar
def contnum(num):
    for i in range(1,num+1):  # de 1 até o número final + 1
        print(i)

contnum(15)



# função while
def contwhile():
    count=0  # para não se tornar um loop infinito
    while count<3:
        print(count)
        count+=1

contwhile()