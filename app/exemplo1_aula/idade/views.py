from django.shortcuts import render

# Create your views here.


def home(request):
    mensagem = ""
    conteudo = False

    if request.method == "POST":
        idade_raw = request.POST.get("idade", "")
        try:
            idade = int(idade_raw)
        except (ValueError, TypeError):
            mensagem = "Por favor, insira uma idade válida"
        else:
            if idade >= 18:
                conteudo = True
            else:
                mensagem = "ACESSO RECUSADO: Você é menor de idade!"

    return render(
        request,
        "index.html",

        {
            "mensagem": mensagem,
            "conteudo": conteudo,
        }
    )