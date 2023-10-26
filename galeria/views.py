from django.shortcuts import render

#Página inical da aplicação
def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')