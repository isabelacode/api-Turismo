from django.db import models

class Atracao(models.Model):
    nome = models.TextField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()
    foto = models.ImageField(upload_to='pontos-turisticos', null=True, blank=True)
    
    def __str__(self):
        return self.nome
