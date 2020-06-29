from django.db import models
from django.urls import reverse
# Create your models here.

class Feria(models.Model):
	"""docstring for Feria"""
	feria_id = models.CharField(max_length=10,help_text="Ingrese ID de la Feria",primary_key=True)
	feria_calle = models.CharField(max_length=200, help_text="Ingrese Nombre de la Calle de la Feria")
	feria_comuna=models.CharField(max_length=200,help_text="Ingrese el Comuna de la feria")
	feria_direccion_ini=models.CharField(max_length=200, help_text="Ingrese la Direccion Inicial de la feria")
	feria_direccion_fin=models.CharField(max_length=200, help_text="Ingrese la Direccion Final de la feria")
	feria_horario_ini=models.CharField(max_length=200, help_text="Ingrese la Horario Inicial de la feria")
	feria_horario_fin=models.CharField(max_length=200, help_text="Ingrese la Horario Final de la feria")
	feria_dias=models.CharField(max_length=200, help_text="Ingrese dias de la feria")
	feria_imagen=models.ImageField(upload_to="gallery", null=True)

	def __str__(self):
		return self.feria_calle

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('ferias:details', args=[str(self.feria_id)])
