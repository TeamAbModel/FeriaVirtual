from django import forms

from .models import Feria

class FeriaCreateForm(forms.ModelForm):
	"""docstring for FeriaCreateForm"""
	feria_id = forms.CharField(label = "ID", required=True,
					widget = forms.TextInput(
						attrs={
							"placeholder":"Ingrese la id de la feria",
							"minlength":3
						}
					)
				)
	feria_calle = forms.CharField(label="Nombre calle", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese el nombre de la calle de la feria",
                            "minlength":5
                        }
                )   
            )
	feria_comuna = forms.CharField(label="Comuna feria", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese el comuna de la feria",
                            "minlength":5
                        }
                	)	 
                )
	feria_direccion_ini = forms.CharField(label="Direccion inicio feria", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese la direccion de inicio de la feria",
                            "minlength":5
                        }
                	)	 
                )
	feria_direccion_fin = forms.CharField(label="Direccion fin feria", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese la direccion del termino de la feria",
                            "minlength":5
                        }
                	)   
            	)
	feria_horario_ini = forms.CharField(label="Horario inicio feria", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese el horario de inicio de la feria",
                            "minlength":5
                        }
                	)   
            	)
	feria_horario_fin = forms.CharField(label="Horario fin feria", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese el horario de termino de la feria",
                            "minlength":5
                        }
                	)   
            	)
	feria_dias = forms.CharField(label="Dias feria", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese dias de funcionamiento de la feria",
                            "minlength":5
                        }
                	)   
            	)
	feria_imagen = forms.ImageField(label="Imagen principal")
	

	class Meta:
		"""docstring for Meta"""
		model = Feria
		fields = [
			'feria_id',
			'feria_calle',
			'feria_comuna',
			'feria_direccion_ini',
			'feria_direccion_fin',
			'feria_horario_ini',
			'feria_horario_fin',
			'feria_dias',
			'feria_imagen'
		]