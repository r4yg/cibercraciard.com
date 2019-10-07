from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin

from django.contrib import admin

# importando modelos
from .models import Param, Subscriber, Provincia, Municipio, ResultadoPrimaria

# arreglo de modelos a registrar
register_models = [
	Param,
	Subscriber,
]

# registrando modelos
admin.site.register(register_models)


"""#=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=#"""

# creando el mixing para Provincia
class ProvinciaResource(ModelResource):
	class Meta:
		model = Provincia
class ProvinciaAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ProvinciaResource

# Registrando
admin.site.register(Provincia, ProvinciaAdmin)

"""#=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=#"""

# creando el mixing para Municipio
class MunicipioResource(ModelResource):
	class Meta:
		model = Municipio
class MunicipioAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = MunicipioResource

# Registrando
admin.site.register(Municipio, MunicipioAdmin)

"""#=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=#"""

# creando el mixing para ResultadoPrimaria
class ResultadoPrimariaResource(ModelResource):
	class Meta:
		model = ResultadoPrimaria
class ResultadoPrimariaAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ResultadoPrimariaResource

# Registrando
admin.site.register(ResultadoPrimaria, ResultadoPrimariaAdmin)

"""#=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=#"""
