from django.shortcuts import render
from .models import Livro


# Create your views here.
del lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/templates/livros/lista.html', {'livros': livros})