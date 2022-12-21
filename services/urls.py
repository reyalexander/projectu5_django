from django.contrib import admin
from django.urls import path
from rest_framework import routers
from . import views
from .api import ServiciosViewSet

router = routers.DefaultRouter()

router.register(r'servicios',ServiciosViewSet, 'serviciosCustom')

'''urlpatterns = [
    #path('task/complete/<id>', views.complete_task),
    #path('moneda/', views.TodoViewSet.as_view({'get': 'list'})),
]'''

urlpatterns = router.urls