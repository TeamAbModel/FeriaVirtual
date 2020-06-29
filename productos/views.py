from django.shortcuts import render
from .models import Producto
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from .forms import ProductoCreateForm
# Create your views here.

class IndexView(generic.ListView):
    model = Producto
    template_name = 'productos/productos_lista.html'
    def get_queryset(self):
        return Producto.objects.all() 

class DetailView(generic.DetailView):
	model = Producto

def ProductoCreate(request):
	form = ProductoCreateForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit = True)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		'title' : "Crear",
		'form':form
	}
	return render(request, 'productos/producto_crear.html',context)

def ProductoSearch(request, id=None):

	queryset = Producto.objects.all()
	query = request.GET.get("q")
	if query:
			queryset = queryset.filter(producto_id__icontains=query)
	context = {
		"object_list" : queryset,
		"title" : "Buscar"
	}
	return render(request, "productos/productos_buscar.html",context)

def ProductoUpdate(request, pk = None):
    instance = get_object_or_404(Producto, producto_id = pk)
    form = ProductoCreateForm(request.POST or None, request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=True)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "Editar",
        "instance":instance,
        "form" : form
    }
    return render(request, "productos/producto_crear.html",context)


def ProductoDelete(request, pk= None):
    instance = get_object_or_404(Producto, producto_id = pk)
    instance.delete()
    return redirect("productos:buscar")