"""
1.	Verificação de login básico
●	Pergunte ao usuário um nome de usuário.
●	Se for igual a "admin", exiba "Acesso permitido".
●	Caso contrário, não mostro e nada (por enquanto).
"""

login = input("Insira a senha para logar: ")


if login == "admin":
    print("Acesso permitido")

