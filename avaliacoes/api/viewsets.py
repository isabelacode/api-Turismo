from rest_framework import viewsets
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacoesViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer