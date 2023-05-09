from django.db import models

# Create your models here.
class Jogos(models.Model):
    jogo = models.CharField(max_length=150)
    plataforma = models.CharField(max_length=100)
    desenvolvedor = models.CharField(max_length=150)