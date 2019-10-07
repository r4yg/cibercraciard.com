from django.shortcuts import render, redirect
from django.contrib import messages

from .utils import Utils as Ut

from .models import Subscriber, ResultadoPrimaria

from .forms import SubscriberForm
from django.db.models import Count, Sum

def landing(request):
	pass

def building(request):
	# pagina temporal a espera de puesta en circulación del portal

	ut = Ut()

	data = {
		"release_time" : ut.get_release_date()
	}

	# adquiriendo la fecha en que se va a publicar la plataforma
	form = SubscriberForm(request.POST or None)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			messages.success(request, "Su correo ha sido registrado, gracias por su interés, pronto estaremos enviando comunicaciones y boletines.")
		else:
			messages.error(request, str(form.errors['email'].as_text()))

	return render(request, "building.html", data)

def results(request):

	resultados = ResultadoPrimaria.objects.all()


	ut = Ut()
	total_mesas = ut.get_param("total_mesas")
	registradas = resultados.aggregate(total_mesas=Count('mesa'))
	por_computadas = round((int(registradas['total_mesas']) / int(total_mesas))*10000)/100

	# Sumando Votos Leonel
	leonel = resultados.aggregate(total=Sum('votos_leonel'))

	# Sumando Votos Gonzalo
	gonzalo = resultados.aggregate(total=Sum('votos_gonzalo'))

	# Sumando votos de ambos
	total = leonel['total'] + gonzalo['total']

	# Calculando porciento Leonel
	por_leonel = round((int(leonel['total']) / int(total))*10000)/100

	# Calculando porciento Gonzalo
	por_gonzalo = round((int(gonzalo['total']) / int(total))*10000)/100

	data = {
		"resultados":       resultados,
		"mesas_computadas": registradas['total_mesas'],
		"por_computadas":   por_computadas,
		"total_mesas":      total_mesas,
		"leonel":           leonel['total'],
		"gonzalo":          gonzalo['total'],
		"por_leonel":       por_leonel,
		"por_gonzalo":      por_gonzalo,
	}

	return render(request, "resultados.html", data)



def detalle_acta(request, res_id):
	try:
		resultado = ResultadoPrimaria.objects.get(id=res_id)
	except:
		messages.error(request, "Seleccione el acta con el boton")
		return redirect("/results")

	data = {
		"resultado" : resultado,
	}
	return render(request, "detalle_acta.html", data)



def error_404_view(request, exception):
	data = {}

	return render(request, "error_404_view.html", data)

def error_500_view(request):
	data = {}

	return render(request, "error_404_view.html", data)