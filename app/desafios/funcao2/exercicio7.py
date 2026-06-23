"""
7. Função que valida senha 

Peça ao usuário uma senha. 
Enquanto a senha for diferente de "python123", repita com while. 
"""

def validar(senha):
    while True:
        if senha == "python123":
            print("Senha correta!")
            break
        else:
            input("Senha incorreta!")

validar(input("Digite a senha: "))