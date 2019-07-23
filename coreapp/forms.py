from django import forms
from .models import Subscriber


""" # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- # """
class SubscriberForm(forms.ModelForm):
	class Meta:
		model = Subscriber
		labels = {
			"email": "Correo Electrónico",
		}
		fields = [
			"email",

		]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['email'].error_messages['required'] = "Información requerida"
		self.fields['email'].error_messages['unique']   = "El correo electrónico suministrado ya está registrado"




