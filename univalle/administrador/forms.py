# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.auth.models import User
from univalle.administrador.models import *
from univalle.home.models import *


class CorreoForm(forms.Form):
	correo	= forms.EmailField(label="Correo Electrónico",widget=forms.TextInput(attrs={'required': True,'type':"email",'class':"form-control",'placeholder':"Para:"}))
	asunto	= forms.CharField(label="Asunto",widget=forms.TextInput(attrs={'required': True,'type':"text",'class':"form-control",'placeholder':'Ingrese Asunto'}))
	texto	= forms.CharField(label="Mensaje",widget=forms.Textarea(attrs={'required': True,'class':"textarea",'cols':100, 'placeholder':'Ingrese Mensaje'}))

class RegistroUsuarioForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':"Ingrese Usuario"}))
	email = forms.EmailField(label="Correo Electrónico",widget=forms.TextInput(attrs={'type':"text",'class':"form-control",'placeholder':"Ingrese Correo Electrónico"}))
	password_one = forms.CharField(label="Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':"Ingrese Contraseña"}))
	password_two = forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':"Confirme Contraseña"}))
		
	#validar si ya existe el correo 
	# def clean_email(self):
	# 	email = self.cleaned_data['email']
	# 	try:
	# 		u = User.objects.get(email=email)
	# 	except User.DoesNotExist:
	# 		return email #para que valide el formulario como si fuera correcto
	# 	raise forms.ValidationError('Correo ya registrado')
		
class EditarUsuarioForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':"Ingrese Usuario",'readonly':"readonly"}))
	email = forms.EmailField(label="Correo Electrónico",widget=forms.TextInput(attrs={'type':"text",'class':"form-control",'placeholder':"Ingrese Correo Electrónico"}))

class CarreraForm(forms.Form):
    codigo = forms.IntegerField(label="Código",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese Código'}))
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'required': True,'type':"text",'class':"form-control",'placeholder':'Ingrese Nombre'}))

class EditarCarreraForm(forms.Form):
    codigo = forms.IntegerField(label="Código",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese Código','readonly':"readonly"}))
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'required': True,'type':"text",'class':"form-control",'placeholder':'Ingrese Nombre'}))

class RegistroInscripcionesForm(forms.Form):
	cedula = forms.IntegerField(label='Cédula',widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese Número de Cédula'}))
	nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Nombres'}))
	apellido = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Apellidos'}))
	snp = forms.CharField(label='Número de Registro ICFES',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese su número de Registro ICFES'}))
	ref_pago = forms.IntegerField(label='Referencia de Pago',widget=forms.TextInput(attrs={'required': True,'type':"number", 'class':"form-control",'placeholder':'Ingrese referencia de pago'}))
	programas_academicos= forms.ModelChoiceField(label='Seleccione la Carrera',widget=forms.Select(attrs={'required': True,'class':"form-control"}), queryset=programasAcademico.objects.all())

class EditarInscripcionesForm(forms.Form):
	cedula = forms.IntegerField(label='Cédula',widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese Número de Cédula','readonly':"readonly"}))
	nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Nombres'}))
	apellido = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Apellidos'}))
	snp = forms.CharField(label='Número de Registro ICFES',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese su número de Registro ICFES'}))
	ref_pago = forms.IntegerField(label='Referencia de Pago',widget=forms.TextInput(attrs={'required': True,'type':"number", 'class':"form-control",'placeholder':'Ingrese referencia de pago'}))
	programas_academicos= forms.ModelChoiceField(label='Seleccione la Carrera',widget=forms.Select(attrs={'required': True,'class':"form-control"}), queryset=programasAcademico.objects.all())

class EditarPasswordForm(forms.Form):
	password_actual = forms.CharField(label="Contraseña Actual",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':"Ingrese Contraseña Actual"}))
	password_one = forms.CharField(label="Nueva Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':"Ingrese Nueva Contraseña"}))
	password_two = forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':"Confirme Nueva Contraseña"}))
