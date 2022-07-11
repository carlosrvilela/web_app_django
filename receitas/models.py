from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome_receita = models.CharField(max_length = 250)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.ImageField()
    rendimento = models.CharField(max_length = 150)
    categoria = models.CharField(max_length = 150)
    data_receita = models.DateField(default = datetime.now, blank = True)
