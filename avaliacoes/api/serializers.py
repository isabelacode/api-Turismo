from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao, Estrela
from rest_framework import serializers

class EstrelaSerializer(ModelSerializer):
    class Meta:
        model = Estrela
        fields = 'estrelas'

class AvaliacaoSerializer(ModelSerializer):
    estrelas= serializers.SerializerMethodField()
    def get_estrelas(self, obj):
        estrelas = obj.estrelas.all()
        total = 0
        for estrela in estrelas:
            total+= estrela.estrelas
        return estrelas.count()/total
    class Meta:
        model = Avaliacao
        fields = ['user', 'comentario', 'nota', 'estrelas']
        