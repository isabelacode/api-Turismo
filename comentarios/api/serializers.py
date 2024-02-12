from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
        read_only_fields = ['likes', 'dislikes']
        
    @receiver(m2m_changed, sender=Comentario.likes.through)
    def ensure_exclusive_likes(sender, instance, action, **kwargs):
        if action == 'pre_add':
            user = kwargs['pk_set'].pop() 
            if user in instance.dislikes.all():
                instance.dislikes.remove(user)  