from django.urls import path
from .views import *

app_name = 'ferias'

urlpatterns = [
	path('',IndexView.as_view(), name='allfairs'),
	path('<str:pk>/', DetailView.as_view(), name='details'),
	path('mantenedor/create/', FeriaCreate, name='crear'),
	path('mantenedor/buscar/', FeriaSearch, name='buscar'),
	path(r'mantenedor/editar/<pk>/', FeriaUpdate, name='editar'),
	path(r'mantenedor/Eliminar/<pk>/', FeriaDelete, name='eliminar'),
]
