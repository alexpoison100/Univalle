# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.auth.models import User
from univalle.administrador.models import *
from univalle.home.models import *

class RegistroUsuarioForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':"Ingrese Usuario"}))
	email = forms.EmailField(label="Correo Electrónico",widget=forms.TextInput(attrs={'type':"text",'class':"form-control",'placeholder':"Ingrese Correo Electrónico"}))
	password_one = forms.CharField(label="Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':"Ingrese Contraseña"}))
	password_two = forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':"Confirme Contraseña"}))
		
	#validar si ya existe el correo 
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email #para que valide el formulario como si fuera correcto
		raise forms.ValidationError('Correo ya registrado')
		
class EditarUsuarioForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':"Ingrese Usuario"}))
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
	snp = forms.CharField(label='Código SNP',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese su SNP'}))
	programas_academicos= forms.ModelChoiceField(label='Seleccione la Carrera',widget=forms.Select(attrs={'required': True,'class':"form-control"}), queryset=programasAcademico.objects.all())

class EditarInscripcionesForm(forms.Form):
	cedula = forms.IntegerField(label='Cédula',widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese Número de Cédula','readonly':"readonly"}))
	nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Nombres'}))
	apellido = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Apellidos'}))
	snp = forms.CharField(label='Código SNP',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese su SNP'}))
	programas_academicos= forms.ModelChoiceField(label='Seleccione la Carrera',widget=forms.Select(attrs={'required': True,'class':"form-control"}), queryset=programasAcademico.objects.all())
