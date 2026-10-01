from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Produto
from .serializers import ProdutoSerializer
from .filters import ProdutoFilter

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = ProdutoFilter

    # Adicione 'marca' em ambos:
    ordering_fields = ("nome", "preco", "marca", "estoque", "descricao")
    search_fields = ("nome", "marca", "descricao")