from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Estrela(models.Model):
    avaliacoes = models.ManyToManyField('Avaliacao', related_name='estrelas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estrelas = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    
class Avaliacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Avaliação de {self.user.username}'




   
