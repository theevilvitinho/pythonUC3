"""8. Função que conta números pares em um intervalo 

Exemplo: contar_pares(1, 20) → quantos pares existem? 

"""

def contar_pares(de,ate):
    quantidade = 0
    for num in range(de,ate+1):
        if num % 2 == 0:
            quantidade += 1
            print(f"De {de} até {ate} existem {quantidade} pares")
    return quantidade



print(contar_pares(1,84))