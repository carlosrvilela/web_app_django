from django.shortcuts import get_object_or_404, render
from .models import Receita

def index(request):
    receitas = Receita.objects.filter(publicar=True).order_by('-data_receita')
    dados = {
        'receitas' : receitas
    }
    
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_exibida = {
        'receita': receita,
    }
    return render(request, 'receita.html', receita_exibida)
