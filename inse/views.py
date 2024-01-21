from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters

from .models import Inse
from .serializers import InseSerializer

# Create your views here.


class InseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Inse.objects.all()
    serializer_class = InseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = '__all__'
    search_fields = ['NO_ESCOLA']
    ordering_fields = '__all__'
    ordering=['id']
