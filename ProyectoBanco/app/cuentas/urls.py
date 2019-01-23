from django.urls import path

from . import views

urlpatterns = [
    path('', views.principal, name = 'cuentas'),
    path('nuevo', views.crear),
    path('editar', views.modificar),
    path('eliminar', views.eliminar),
]