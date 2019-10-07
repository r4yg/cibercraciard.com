from django.urls import path, include
from . import views

app_name = 'coreapp'

urlpatterns = [
	path('', views.building, name='building'),
	path('results', views.results, name='results'),
	path('detalle_acta/<int:res_id>', views.detalle_acta, name='detalle_acta'),

	
]
