from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
import pdfkit

from app import cuentas
from .forms import FormularioCliente
from .forms import FormularioCuenta
from .forms import FormularioTransaccion
from app.modelo.models import Cliente
from app.modelo.models import Cuenta
from app.modelo.models import Transaccion
from reportlab.pdfgen import canvas

from django.conf import settings
from io import BytesIO
from django.views.generic import View

# Create your views here.

def principal(request):
    listaClientes = Cliente.objects.all().order_by('apellidos')
    context = {
        'clientes': listaClientes,
        'title': "Clientes",
        'mensaje': "Modulo Clientes"
    }
    return render(request, 'clientes/home_cliente.html', context)

def saludar(request):
    return HttpResponse('Hola clase')


def crear(request):
    formulario = FormularioCliente(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            cliente = Cliente()
            cliente.cedula = datos.get('cedula')
            cliente.apellidos = datos.get('apellidos')
            cliente.nombres = datos.get('nombres')
            cliente.genero = datos.get('genero')
            cliente.estadoCivil = datos.get('estadoCivil')
            cliente.fechaNacimiento = datos.get('fechaNacimiento')
            cliente.correo = datos.get('correo')
            cliente.telefono = datos.get('telefono')
            cliente.celular = datos.get('celular')
            cliente.direccion = datos.get('direccion')
            cliente.save()
            return redirect(principal)
    context = {
        'f': formulario,
        'title': "Ingresar Cliente",
        'mensaje': "Ingresar Nuevo Cliente"
    }
    return render(request, 'clientes/crear_cliente.html', context)

def modificar(request):
    dni = request.GET['cedula']
    cliente = Cliente.objects.get(cedula=dni)
    formulario = FormularioCliente(request.POST, instance=cliente)

    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            cliente.cedula = datos.get('cedula')
            cliente.apellidos = datos.get('apellidos')
            cliente.nombres = datos.get('nombres')
            cliente.genero = datos.get('genero')
            cliente.estadoCivil = datos.get('estadoCivil')
            cliente.fechaNacimiento = datos.get('fechaNacimiento')
            cliente.correo = datos.get('correo')
            cliente.telefono = datos.get('telefono')
            cliente.celular = datos.get('celular')
            cliente.direccion = datos.get('direccion')
            cliente.save()
            return redirect(principal)
    context = {
        'f': formulario,
        'title': "Modificar Cliente",
        'mensaje': "Modificar datos de " + cliente.nombres + " " + cliente.apellidos
    }
    return render(request, 'clientes/crear_cliente.html', context)

def eliminar(request):
    dni = request.GET['cedula'];
    cliente = Cliente.objects.get(cedula=dni)
    if cliente:
        if cliente.delete():
            return HttpResponse('eliminado')
        else:
            return HttpResponse('no eliminado')
    else:
        return HttpResponse('perdido')
    return render(request, 'clientes/home_cliente.html', context)

def principalCuenta(request):
    listaCuentas = Cuenta.objects.all().order_by('numero')
    context = {
        'cuentas': listaCuentas,
        'title': "Cuentas",
        'mensaje': "Modulo Cuentas"
    }
    return render(request, 'cuentas/cuentas.html', context)

def principalTransaccion(request):
    listaTransacciones = Transaccion.objects.all().order_by('fecha')
    context = {
        'transacciones': listaTransacciones,
        'title': "Transaccion",
        'mensaje': "Modulo Transaccion"
    }
    return render(request, 'transaccion/transaccion.html', context)

def crearCuenta(request):
    formulario = FormularioCuenta(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            cuenta = Cuenta()
            cuenta.numero = datos.get('numero')
            cuenta.estado = datos.get('estado')
            cuenta.saldo = datos.get('saldo')
            cuenta.tipoCuenta = datos.get('tipoCuenta')
            cuenta.cliente = datos.get('cliente')

            cuenta.save()
            return redirect(principalCuenta)
    context = {
        'f': formulario,
        'title': "Ingresar Cuenta",
        'mensaje': "Ingresar Nuevo Cuenta"
    }
    return render(request, 'cuentas/crear_cuentas.html', context)

@login_required
def crearTransaccion(request):
    formulario = FormularioTransaccion(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            transaccion = Transaccion()
            transaccion.tipo = datos.get('tipo')
            transaccion.valor = datos.get('valor')
            transaccion.cuenta = datos.get('cuenta')
            numeroCuenta = datos.get('cuenta')
            transaccion.descripcion = datos.get('descripcion')
            transaccion.responsable = datos.get('responsable')
            print(datos.get('tipo'))
            print(numeroCuenta)
            if (datos.get('tipo') == 'deposito'):

                print('entro en deposito')
                dni = numeroCuenta
                cuenta = Cuenta.objects.get(numero=dni)
                print(cuenta.numero)
                formularioC = FormularioCuenta(instance=cuenta)

                #datosC = formularioC.cleaned_data

                Cnumero = cuenta.numero
                Cestado = cuenta.estado
                Csaldo = cuenta.saldo
                Ctipo = cuenta.tipoCuenta
                Ccliente = cuenta.cliente

                cuenta.numero = Cnumero
                cuenta.estado = Cestado
                saldo = Csaldo + transaccion.valor
                cuenta.saldo = saldo
                print(cuenta.saldo)
                cuenta.tipoCuenta = Ctipo
                cuenta.cliente = Ccliente
                cuenta.save()
                transaccion.save()
            if (datos.get('tipo') == 'retiro'):
                print('entro en retiro')
                dni = datos.get('cuenta')
                cuenta = Cuenta.objects.get(numero=dni)
                formularioC = FormularioCuenta(instance=cuenta)
                #datosC = formularioC.cleaned_data

                Cnumero = cuenta.numero
                Cestado = cuenta.estado
                Csaldo = cuenta.saldo
                Ctipo = cuenta.tipoCuenta
                Ccliente = cuenta.cliente

                cuenta.numero = Cnumero
                cuenta.estado = Cestado
                saldo = Csaldo - transaccion.valor
                cuenta.saldo = saldo
                print(cuenta.saldo)
                cuenta.tipoCuenta = Ctipo
                cuenta.cliente = Ccliente
                cuenta.save()
                transaccion.save()
            if (datos.get('tipo') == 'transferencia'):

                print('entro en transaferencia')
                dni = numeroCuenta
                cuenta = Cuenta.objects.get(numero=dni)
                print(cuenta.numero)

                Cnumero = cuenta.numero
                Cestado = cuenta.estado
                Csaldo = cuenta.saldo
                Ctipo = cuenta.tipoCuenta
                Ccliente = cuenta.cliente

                cuenta.numero = Cnumero
                cuenta.estado = Cestado
                saldo = Csaldo + transaccion.valor
                cuenta.saldo = saldo
                print(cuenta.saldo)
                cuenta.tipoCuenta = Ctipo
                cuenta.cliente = Ccliente
                cuenta.save()
                transaccion.save()
            return redirect(principalTransaccion)
    context = {
        'f': formulario,
        'title': "Ingresar Transaccion",
        'mensaje': "Ingresar Nueva Transaccion"
    }
    return render(request, 'transaccion/crear_transaccion.html', context)

@login_required
def transferencia(request, valor):
    cuenta = Cuenta.objects.get(numero=valor)
    if request.method == 'GET':
        formulario = Cuenta(request.POST, instance=cuenta)
    else:
        formulario = Cuenta(request.POST, instance=cuenta)
        if formulario.is_valid():
            formulario.save()



@login_required
def pdf (request):
    listaCli = Cliente.objects.all().order_by('apellidos')
    listaCue = Cuenta.objects.all().order_by('numero')
    listaTra = Transaccion.objects.all().order_by('fecha')

    cliente = canvas.Canvas("Clientes.pdf")
    cuenta = canvas.Canvas("Cuentas.pdf")
    transaccion = canvas.Canvas("Transaciones.pdf")

    cliente.drawString(100, 750, "pdf de los clientes")
    #cuenta.drawString(100, 750, listaCue)
    #transaccion.drawString(100, 750, listaTra)

    cliente.save()
    return render(request, 'clientes/home_cliente.html')
    #cuenta.save()
    #transaccion.save()


def generarPDF (request):

    return render(request, 'clientes/home_cliente.html')
    return


@login_required
def buscarCliente(request):
    usuario = request.user
    print(usuario.get_all_permissions())
    #if usuario.has_perm('modelo.view_cliente'):
    dni = request.GET['txt_buscarCliente']
    listaClientes = Cliente.objects.filter(cedula =dni)
    context = {
        'clientes': listaClientes,
        'title': "Clientes",
        'mensaje': "Modulo Clientes",
        'estado': True
    }
    return render(request, 'clientes/home_cliente.html', context)
    #else:
        #messages.warning(request, 'No Permitido')
        #return render(request, 'login/403.html')

def buscarCuenta(request):
    usuario = request.user
    print(usuario.get_all_permissions())
    if usuario.has_perm('modelo.view_cuenta'):
        dniC = request.GET['txt_buscarCuenta']
        listaCuentas = Cuenta.objects.filter(numero=dniC)
        context = {
            'cuentas': listaCuentas,
            'title': "Cuenta",
            'mensaje': "Modulo Cuenta",
        }
        return render(request, 'cuentas/cuentas.html', context)

def buscarTransacion(request):
    usuario = request.user
    print(usuario.get_all_permissions())
    if usuario.has_perm('modelo.view_transacion'):
        cuentaN = request.GET['txt_buscarTransaccion']
        listaTransaciones = Transaccion.objects.filter(cuenta=cuentaN)
        context = {
            'transacciones': listaTransaciones,
            'title': "Transación",
            'mensaje': "Modulo Transaccion",

        }
        return render(request, 'transaccion/transaccion.html', context)
