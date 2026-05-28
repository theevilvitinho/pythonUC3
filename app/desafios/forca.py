"""
Faça um jogo para o usuário adivinhar qual a palavra secreta. Ex.: forca.

-Usuário poderá didigtar uma letra;;
-Quando o usuário digitar uma letra, o programa deve conferir se a mesma está na palavra secreta (função len);
-Se a letra digitada não estiver na palavra, exiba "*";
-Se a letra digitada estiver na palavra secreta, exiba a letra;
-Faça a contagem de tentativas do usuário.

"""

import os


palavra = "onomatopeia"
acertos = ""
tentativas = 0
letra_errada = ""


while True:
    letra = input("Digite uma letra: ")
    letra = letra.lower() # As letras sempre serão minúsculas
    tentativas += 1

    # Verificar erros:
    if letra in acertos:
        print("Você já acertou essa letra")
        continue

    if letra in letra_errada:
        print("Você já tentou essa letra")
        continue


    # Verificar se a letra existe
    if len(letra) > 1:
        print("Digite apenas uma letra")
        continue # Sempre que digitar mais de uma letra, voltará ao início da pergunta

    if letra in palavra:
        acertos += letra # Se a letra estiver na palavra, a letra certa será exibida
        print("Letra correta")
    
    else:
        print("A letra está incorreta")
        letra_errada += 1 # Caso a letra esteja errada, a mesma será adicionada na biblioteca de letras erradas


    # Monta a palavra escondida

    palavra_formada = ""

    for acertos in palavra:
        if palavra in acertos: 
            palavra_formada += palavra # Para cada letra certa, as mesmas serão adicionadas na palavra completa

    # Exibe informaçõesdo jogo
    print("\n--------------------------------------------------")
    print(f"Palavra: {palavra}")
    print(f"Letras erradas: {letra_errada}")
    print(f"Tentativas: {tentativas}")
    print("----------------------------------------------------")

    # Verificar vitória
    if palavra_formada == palavra:
        os.system("cls" if os.name == "nt" else "clear")
        print("Você ganhou!")
        print(f"A palavra era: {palavra}")
        print(f"Total de tentativas: {tentativas}")
        break  # Encerra o jogo, caso contrário voltaria ao início

print("\n Jogo encerrado!")