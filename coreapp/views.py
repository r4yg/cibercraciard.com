from django.shortcuts import render
from django.contrib import messages

from .utils import Utils as Ut

from .models import Subscriber

from .forms import SubscriberForm

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

