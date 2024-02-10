from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from comentarios.models import Comentario
from .serializers import ComentarioSerializer

class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    @action(detail=True, methods=['post'])
    def toggle_reaction(self, request, pk=None):
        comentario = self.get_object()
        user = request.user

        if user in comentario.likes.all():
            comentario.dislike.remove(user)
        elif user in comentario.dislikes.all():
            comentario.like.remove(user)
        else:
            comentario.likes.add(user)

        comentario.save()
        serializer = self.get_serializer(comentario)
        return Response(serializer.data)