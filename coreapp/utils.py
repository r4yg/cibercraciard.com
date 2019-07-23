
# cargando modelos
from coreapp.models import Param
from datetime import datetime

class Utils():
	"""
	@brief:  colección de utilidades para uso general en el sistema
	@author: r4yg | cibercraciard@gmail.com
	@date:   13.julio.2019
	"""
	def __init__(self):
		self.id_check_url = "https://dgii.gov.do/app/WebApps/ConsultasWeb/consultas/ciudadanos.aspx"
		
		# dgii timeout default info
		self.default_dgii_timeout           = 30
		self.dgii_timeout_param             = "dgii_timeout"
		self.dgii_timeout_param_description = "Cantidad en segundos a esperar por la página de revisión de cédulas de impuestos internos para validar usuarios de la plataforma"

		# mail default info
		self.cibercraciard_default_mail_param       = "cibercracia_mail"
		self.cibercraciard_default_mail_value       = "cibercraciard@gmail.com"
		self.cibercraciard_default_mail_description = "Correo definido por el sistema para recibir informaciones de los usuarios en general"


		self.date_format = "%d-%m-%Y %H:%M"
		self.cibercraciard_default_release_date_param = "release_date"
		self.cibercraciard_default_release_date_value = "01-10-2019 15:00"
		self.cibercraciard_default_release_date_descr = "Fecha de lanzamiento de la primera versión de la plataforma, formato: '{DATE_DORMAT}' ".format(DATE_DORMAT=self.date_format)


	def get_param(self, param):

		return_val = False
		try:
			val        = Param.objects.get(parameter=str(param))
			return_val = val.value
		except:
			pass

		return return_val

	def set_param(self, param, value, description = None):
		# revisando si existe para actualizarlo
		try:
			param = Param.objects.get(parameter=str(param))
		except:
			param = Param(
					parameter = str(param),
					value     = str(value)
				)

		param.value = str(value)
		if description:
			param.description = description
		param.save()

		return param.value


	def get_cibercraciard_mail(self):
		cr_mail = self.get_param(self.cibercraciard_default_mail_param)
		if not cr_mail:
			cr_mail = self.set_param(self.cibercraciard_default_mail_param, self.cibercraciard_default_mail_value, self.cibercraciard_default_mail_description)
		return cr_mail


	def check_gov_id(self, id):
		# revisando identificación en el portal
		# importando las librerias de revision html localmente ya que son algo pesadas y asi dejandola solo par el uso en este método en exclusivo

		from bs4 import BeautifulSoup as bs
		import requests
		from requests.packages.urllib3.exceptions import InsecureRequestWarning

		requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

		dgii_timeout = int(self.get_param(self.dgii_timeout_param))

		if not dgii_timeout:
			dgii_timeout = int(self.set_param(self.dgii_timeout_param, self.default_dgii_timeout, self.dgii_timeout_param_description))

		# adquiriendo el formulario de impuestos internos

		try:
			r = requests.get(self.id_check_url, verify=False, timeout=dgii_timeout)
		except:
			raise Exception("Formulario de revision en DGII no disponible, por favor intente mas tarde o pongase en contacto con cibiercracia escribiendo a: {MAIL}".format(MAIL=self.get_cibercraciard_mail()))
		# revisando los datos del request

		soup = bs(r.text, 'html.parser')
		# estableciendo el payload
		payload = {
			"__VIEWSTATE" : soup.find('input', {'name': '__VIEWSTATE'}).get('value'),
			"__EVENTVALIDATION" : soup.find('input', {'name': '__EVENTVALIDATION'}).get('value'),
			"ctl00$cphMain$txtCedula" : id,
			"ctl00$cphMain$btnBuscarCedula" : "Buscar"
		}
		try:
			r = requests.post(self.id_check_url, data=payload, timeout=dgii_timeout)
		except:
			raise Exception("No fue posible revisar su información en los servicios públicos de DGII, por favor intente mas tarde o pongase en contacto con cibiercracia escribiendo a: {MAIL}".format(MAIL=self.get_cibercraciard_mail()))

		soup = bs(r.text, 'html.parser')

		try:
			table = soup.find('table', {
				'id' : 'ctl00_cphMain_dvResultadoCedula'
				})

			rows = table.find_all('tr')
			return {
				"nombre":    str(rows[0].find_all('td')[1].text).replace('\xa0', ""),
				"estado":    str(rows[1].find_all('td')[1].text).replace('\xa0', ""),
				"tipo":      str(rows[2].find_all('td')[1].text).replace('\xa0', ""),
				"cedula":    str(rows[3].find_all('td')[1].text).replace('\xa0', ""),
				"actividad": str(rows[4].find_all('td')[1].text).replace('\xa0', ""),

			}
		except Exception as e:
			print(str(e))
			return False

		return self.get_cibercraciard_mail()


	def get_release_date(self):
		release_date = self.get_param(self.cibercraciard_default_release_date_param)
		if not release_date:
			release_date = self.set_param(self.cibercraciard_default_release_date_param, self.cibercraciard_default_release_date_value, self.cibercraciard_default_release_date_descr)

		datetime_obj = datetime.strptime(release_date, self.date_format)

		time_left = datetime_obj - datetime.now()

		release_on = {
			"days":    time_left.days,
			"hours":   int(time_left.seconds / 3600 ),
			"minutes": int(((time_left.seconds / 3600) - int(time_left.seconds / 3600 ))*60 ),
			"seconds": int(((time_left.seconds / 60) - int(time_left.seconds / 60 ))*60)
		}

		return release_on




