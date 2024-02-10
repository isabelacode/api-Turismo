from rest_framework import viewsets
from atracoes.models import Atracao
from .serializers import AtracaoSerializer

class AtracoesViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filterset_fields = ('nome', 'descricao')