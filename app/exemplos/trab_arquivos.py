import subprocess



# arquivo = open("app\exemplos\dados.txt","r")
# conteudo = arquivo.read()
# print(conteudo)
# arquivo.close


try:
    with open("app\exemplos\dados.txt","r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

except FileExistsError:
    print("Arquivo não encontrado")

# Sobrescrever

with open("app\exemplos\dados.txt","w") as arquivo:
    arquivo.write("Bem-vindos ao Python")



# Adicionar novo conteúdo

with open("app\exemplos\dados.txt","a") as arquivo:
    arquivo.write(" Usuário logado\n")



# Abrindo em um programa da minha escolha

subprocess.Popen(["code","app\exemplos\dados.txt"])