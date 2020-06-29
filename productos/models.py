from django.db import models
from django.urls import reverse
# Create your models here.

class Producto(models.Model):
	"""docstring for Producto"""
	producto_id = models.CharField(max_length=10,help_text="Ingrese ID del producto",primary_key=True)
	producto_nombre = models.CharField(max_length=200, help_text="Ingrese Nombre de la producto")
	producto_valor=models.IntegerField(help_text="Ingrese el precio de la producto (Ej: $ 999 999).")
	producto_descripcion=models.TextField(max_length=3000, help_text="Ingrese la descripcion de la producto")
	producto_imagen=models.ImageField(upload_to="gallery", null=True)

	def __str__(self):
		return self.producto_nombre

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('productos:details', args=[str(self.producto_id)])