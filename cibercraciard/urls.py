from django.contrib import admin
from django.urls import path, include

from django.conf.urls import handler404, handler500
from coreapp import views as coreappviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coreapp.urls', namespace='coreapp')),

]


handler404 = coreappviews.error_404_view
handler500 = coreappviews.error_500_view