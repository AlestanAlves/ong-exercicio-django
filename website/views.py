from django.shortcuts import render
from website.models import *

def index(request):
    if request.method == 'POST':
        data = Coach()
        data.nome = request.POST['nome']
        data.frase = request.POST['frase'] 
        data.inspirador = request.POST['inspirador']
        data.save()
        args = {
            'sucesso': 'Você conseguiu campeão! Grite: Alucinação!'
        }
        return render(request, 'index.html', args)

    return render (request, 'index.html')

def listar_coachs(request):
    listar_coachs = Coach.objects.all()
    args = {
        'listar_coachs': listar_coachs
    }
    return render(request, 'listar_coachs.html', args) 


def recuperar_coach(request, id):
    item = Coach.objects.filter(activate=False).all()
    if item is not None:
        item.ativo = True
        item.save ()
        return redirect('coachs/listar')

# Create your views here.
