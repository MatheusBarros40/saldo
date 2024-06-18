from rest_framework import viewsets
from .models import Categoria, Transacao
from .serializers import CategoriaSerializer, TransacaoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Saldo

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer



class SaldoView(APIView):
    def get(self, request, format=None):
        try:
            saldo = Saldo.objects.first()  # Assume que há apenas um objeto Saldo
            if saldo is not None:
                return Response({'saldo': saldo.valor}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Saldo não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
