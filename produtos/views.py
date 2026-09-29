from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet

from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProdutoFilter
    ordering_fields = ("nome", "preco")
    ordering = ("id",)
    search_fields = ("nome",)