"""
4. Função que imprime números de 1 até N usando WHILE 

Crie uma função contar(n) que utiliza um while para imprimir números até n. 
"""

def contar(inicio,fim):
    atual = inicio
    while atual <= fim:
        print(atual)
        atual += 1

contar(1,8)