"""
Solicite ao usuário que digite 5 números.
Armazene esses números em uma lista.
Ao final, exiba:
•	A lista completa. 
•	A soma dos números digitados.
"""

numeros = []


for x in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

print(f"Lista de números: {numeros}")
print(f"A soma de todos os números: {sum(numeros)}")