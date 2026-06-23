"""
2. Função que retorna o maior de dois números 

Crie uma função maior(a, b) que devolve qual número é maior usando if/else. 
"""

def maior(a,b):
    if a > b:
        print(f"O número {a} é maior que o número {b}")
    elif b > a:
        print(f"O número {b} é maior que o número {a}")
    else:
        print("Os números são iguais")

maior(5,5)