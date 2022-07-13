from django.db import models
from datetime import datetime

from pessoas.admin import Pessoa

class Receita(models.Model):
    nome_receita = models.CharField(max_length = 250)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length = 150)
    categoria = models.CharField(max_length = 150)
    data_receita = models.DateTimeField(default = datetime.now, blank = True)
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE)
    foto_receita = models.ImageField(upload_to = 'fotos/%d/%m/%Y', blank = True)
    publicar = models.BooleanField(default = False)
    
    def __str__(self):
        return self.nome_receita
