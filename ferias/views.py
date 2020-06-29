from django.shortcuts import render
from .models import Feria
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from .forms import FeriaCreateForm

# Create your views here.

class IndexView(generic.ListView):
    model = Feria
    template_name = 'ferias/ferias_lista.html'
    def get_queryset(self):
        return Feria.objects.all() 

class DetailView(generic.DetailView):
	model = Feria

def FeriaCreate(request):
	form = FeriaCreateForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit = True)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		'title' : "Crear",
		'form':form
	}
	return render(request, 'ferias/feria_crear.html',context)

def FeriaSearch(request, id=None):

	queryset = Feria.objects.all()
	query = request.GET.get("q")
	if query:
			queryset = queryset.filter(feria_id__icontains=query)
	context = {
		"object_list" : queryset,
		"title" : "Buscar"
	}
	return render(request, "ferias/ferias_buscar.html",context)

def FeriaUpdate(request, pk = None):
    instance = get_object_or_404(Feria, feria_id = pk)
    form = FeriaCreateForm(request.POST or None, request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=True)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "Editar",
        "instance":instance,
        "form" : form
    }
    return render(request, "ferias/feria_crear.html",context)


def FeriaDelete(request, pk= None):
    instance = get_object_or_404(Feria, feria_id = pk)
    instance.delete()
    return redirect("ferias:buscar")