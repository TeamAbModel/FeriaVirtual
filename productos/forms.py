from django import forms

from .models import Producto

class ProductoCreateForm(forms.ModelForm):
	"""docstring for productoCreateForm"""
	producto_id = forms.CharField(label = "ID", required=True,
					widget = forms.TextInput(
						attrs={
							"placeholder":"Ingrese la ID del producto",
						}
					)
				)
	producto_nombre = forms.CharField(label="Nombre producto", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese el nombre del producto",
                            "minlength":5
                        }
                )   
            )
	producto_valor = forms.IntegerField(label="Precio", required =True,
                    widget=forms.NumberInput(
                        attrs={
                            "placeholder":"Precio producto"
                        }
                    )
                )
	producto_descripcion = forms.CharField(label="Descripcion", required=True,
                widget=forms.Textarea(
                        attrs={
                            "placeholder":"Ingrese descripcion del producto",
                            "maxlength":3000
                        }
                )   
            )
	producto_imagen = forms.ImageField(label="Imagen principal")

	class Meta:
		"""docstring for Meta"""
		model = Producto
		fields = [
			'producto_id',
			'producto_nombre',
			'producto_valor',
			'producto_descripcion',
			'producto_imagen'
		]
			