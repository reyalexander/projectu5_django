from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions,filters, throttling
from django.shortcuts import get_object_or_404
from .pagination import *
from rest_framework.decorators import action
# Añadimos UserRateThrottle
from rest_framework.throttling import UserRateThrottle
import random

class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicioSerializer
    pagination_class = SmallResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['user_id__id','monto','servicio']

    def get_throttles(self):
        if self.action == 'create':
            self.throttle_scope = 'create_servicio'
        return super().get_throttles()

    def create(self, request):
        if isinstance(request.data, list):
            serializer = ServicioSerializer(data=request.data, many = True)
        else:
            serializer = ServicioSerializer(data=request.data)
        
        if serializer.is_valid():
            data=request.data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Services.objects.all()
        serializer = ServicioSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Services.objects.all()
        services = get_object_or_404(queryset, pk=pk)
        serializer = ServicioSerializer(services)
        return Response(serializer.data)