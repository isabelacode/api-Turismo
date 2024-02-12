from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from comentarios.models import Comentario
from .serializers import ComentarioSerializer

class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer