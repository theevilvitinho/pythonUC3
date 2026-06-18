from django.shortcuts import render

# Create your views here.


def home(request):
    mensagem = ""
    conteudo = False

    if request.method == "POST":
        idade = int(request.POST.get("idade"))

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