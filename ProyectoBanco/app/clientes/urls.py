from django.urls import path

from . import views

urlpatterns = [
    path('', views.principal, name = 'cliente'),
    path('primerMensaje', views.saludar),
    path('nuevo', views.crear),
    path('editar', views.modificar),
    path('eliminar', views.eliminar),
    path('nuevaCuenta', views.crearCuenta),
    path('nuevaTrasaccion', views.crearTransaccion),
    path('cuentas', views.principalCuenta),
    path('transaccion', views.principalTransaccion),
    path('pdf', views.pdf),
    path('buscarCliente', views.buscarCliente),
    path('buscarCuenta', views.buscarCuenta),
    path('buscarTransaccion', views.buscarTransacion),
    #path('reporte_personas_pdf', views.ReportePersonasPDF),
#url(r'^reporte_personas_pdf/$',login_required(ReportePersonasPDF.as_view()), name="reporte_personas_pdf"),
]
