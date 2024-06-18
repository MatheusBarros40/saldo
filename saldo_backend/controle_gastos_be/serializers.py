from rest_framework import serializers
from .models import Categoria, Transacao

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']

class TransacaoSerializer(serializers.ModelSerializer):
    
    categoria_detalhes = CategoriaSerializer(source='categoria', read_only=True)
    categoria = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(),
        write_only=True
        )
        
    class Meta:
        model = Transacao
        fields = ['id', 'valor', 'data', 'descricao', 'tipo', 'categoria', 'categoria_detalhes']

