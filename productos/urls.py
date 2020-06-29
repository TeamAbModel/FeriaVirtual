from django.urls import path
from .views import *

app_name = 'productos'

urlpatterns = [
	path('',IndexView.as_view(), name='allproducts'),
	path('<str:pk>/', DetailView.as_view(), name='details'),
	path('mantenedor/create/', ProductoCreate, name='crear'),
	path('mantenedor/buscar/', ProductoSearch, name='buscar'),
	path(r'mantenedor/editar/<pk>/', ProductoUpdate, name='editar'),
	path(r'mantenedor/Eliminar/<pk>/', ProductoDelete, name='eliminar'),
]