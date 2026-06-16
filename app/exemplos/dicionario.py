pessoa = {
    "nome": "Ana",
    "cpf": "234.769.053-08",
    "telefone": 21956439002,
}

print(pessoa)
print(pessoa["cpf"])  # Mostrar apenas esse valor
pessoa["nome"] = "Luigi"  # Mudar o valor
print(pessoa["nome"])

for chave, valor in pessoa.items():
    print(f"Seu {chave} é {valor}")

pessoa.update({"nome": "Jair", "cpf": "555.776.545-09", "telefone":21940038928})
print(pessoa)