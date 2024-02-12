from django.contrib import admin
from .models import Comentario
from .actions import reprova_comentarios, aprova_comentarios

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['user', 'data', 'aprovado', 'count_likes', 'count_dislikes']
    actions = [reprova_comentarios, aprova_comentarios]
    
admin.site.register(Comentario, ComentarioAdmin)