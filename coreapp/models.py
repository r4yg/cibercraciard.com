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