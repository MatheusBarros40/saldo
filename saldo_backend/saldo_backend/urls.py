from django.urls import path, include
from rest_framework.routers import DefaultRouter
from controle_gastos_be.views import CategoriaViewSet, TransacaoViewSet, SaldoView # type: ignore

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'transacoes', TransacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('saldo/', SaldoView.as_view(), name='saldo'),
]
