from django import forms
from app.modelo.models import Cliente
from app.modelo.models import Cuenta
from app.modelo.models import Banco
from app.modelo.models import Transaccion

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["cedula", "nombres", "apellidos", "genero", "estadoCivil", "fechaNacimiento", "correo", "telefono", "celular", "direccion"]

class FormularioBanco(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ["nombre", "direccion", "telefono", "correo"]

class FormularioCuenta(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ["numero", "estado", "saldo", "tipoCuenta", "cliente"]

class FormularioTransaccion(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ["tipo", "valor", "descripcion", "responsable", "cuenta"]
