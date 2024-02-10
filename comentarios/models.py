from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)
    estrelas = models.FloatField(blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    likes = models.ManyToManyField(User, related_name='comentario_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='comentario_dislikes', blank=True)

    def __str__(self):
        return self.user.username

    def count_likes(self):
        return self.likes.count()

    def count_dislikes(self):
        return self.dislikes.count()