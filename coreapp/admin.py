from django.contrib import admin

# importando modelos
from .models import Param, Subscriber

# arreglo de modelos a registrar
register_models = [
	Param,
	Subscriber,
]

# registrando modelos
admin.site.register(register_models)
