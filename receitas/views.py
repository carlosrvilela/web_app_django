from django.shortcuts import render

def index(request):
    receitas = {
        1: 'Lasanha',
        2: 'Sopa',
        3: 'Sorvete',
        4: 'Bolo'
    }
    dados = {
        'nomes_receitas' : receitas
    }
    
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
