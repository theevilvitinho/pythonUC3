nome = "Vitor"
listaNomes = ["Claúdio","André","Julia","Ronaldo","Jéssica"]
print(nome)
print(listaNomes)
print(len(listaNomes)) # Conta quantos elementos existem
listaNomes.append("Almir") # Adiciona um novo item na lista
print(listaNomes)
print(listaNomes.index("André")) # Recupera o index da pesquisa
nova_lista = [1,5,"Kyo","Iory"] # Lista heterogênea
print(nova_lista)
#nova_lista.remove(1) # Remove item da lista
#nova_lista.remove("Kyo") 
nova_lista.reverse() # Reverte a ordem da lista
print(nova_lista)
nova_lista.append([10,50,9]) # Adiciona uma lista dentro de outra lista
print(nova_lista)
compras = ["Arroz","Pizza","Bife","Refrigerante","Frango"]
print("Arroz" in compras) # Arroz está na lista compras
print(compras[0]) # Retorna o item da lista
print("Uva" not in compras) # Uva não está na lista compras?
print(compras[-1])
numeros = [5,3,1,4,2]
#print(numeros.sort()) # Ordenação crescente
#numeros.sort(reverse=True) # Ordenação descrescente

listaNumero2 = numeros.copy() #   Copiar lista

# Fatia lista
n1 = numeros[0]
n2 = numeros[1]

#ou
print(numeros[1:5])

#numeros.clear() # Remove todos os itens da lista

print(numeros.pop(2)) # Remove o item pelo index
print(numeros)
