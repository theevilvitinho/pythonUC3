"""
1. Função que verifica se o número é par ou ímpar 

Crie uma função verificar par(num) que receba um número e diga se é par ou ímpar usando if. 
"""

def verificar(num):
    if num % 2 == 0:
        print(f"O número {num} é PAR!")
    else:
        print(f"O número {num} é ÍMPAR!")

verificar(14)