from django.db import models



class Param(models.Model):
	"""
		@brief: modelo para acumular variables de uso del sistema que sun parte de la confiduraciónd el mismo
		@author: R4yG | cibercraciard@gmail.com
		@date: 13.july.2019
	"""
	parameter   = models.CharField(max_length=50, db_index=True, unique=True)
	value       = models.CharField(max_length=254)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return "{NAME}".format(NAME=self.parameter)

class Subscriber(models.Model):
	"""
		@brief: modelo para registrar los suscriptores
		@author: R4yG | cibercraciard@gmail.com
		@date: 13.july.2019
	"""

	email     = models.EmailField(db_index=True, unique=True)
	is_active = models.BooleanField(default=True, db_index=True)
	r_date    = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{NAME}".format(NAME=self.email)

class Provincia(models.Model):
	nombre = models.CharField(max_length=64, db_index=True)

	def __str__(self):
		return "{}".format(self.nombre)

class Municipio(models.Model):
	provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
	cod       = models.CharField(max_length=32, db_index=True)
	nombre    = models.CharField(max_length=64, db_index=True)
	def __str__(self):
		return "{}".format(self.nombre)




class ResultadoPrimaria(models.Model):
	nombre   = models.CharField(max_length=64, null=True)
	apellido = models.CharField(max_length=64, null=True)
	phone    = models.CharField(max_length=14, db_index=True, unique=True)

	municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
	mesa      = models.CharField(max_length=32, db_index=True, null=True)

	votos_gonzalo = models.IntegerField(default=0, db_index=True)
	votos_leonel  = models.IntegerField(default=0, db_index=True)

	acta_imag = models.ImageField(upload_to = 'static/building/images/actas/', null=True)
	# este campo debe ser privado ya que contiene el token del bot
	photo_url = models.CharField(max_length=256, null=True)







