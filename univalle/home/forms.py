# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.auth.models import User
from univalle.home.models import *



class ContactForm(forms.Form):
	Nombre	= forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'type':"text",'class':"form-control"}))
	Correo	= forms.EmailField(label="Correo Electrónico",widget=forms.TextInput(attrs={'type':"email",'class':"form-control",'placeholder':"Ingrese Correo Electrónico"}))
	Asunto	= forms.CharField(label="Asunto",widget=forms.TextInput(attrs={'type':"text",'class':"form-control"}))
	Mensaje	= forms.CharField(label="Mensaje",widget=forms.Textarea(attrs={'class':"form-control",'rows':3}))

class LoginForm(forms.Form):
	Usuario = forms.CharField(widget=forms.TextInput(attrs={'type':"text", 'class':"form-control",'placeholder':'Ingrese Usuario'}))
	Contrasena = forms.CharField(label="Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'class':"form-control",'placeholder':'Ingrese Contraseña'}))

class RegisterForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput(attrs={'type':"text", 'class':"form-control",'placeholder':"Ingrese Usuario"}))
	email = forms.EmailField(label="Correo Electrónico",widget=forms.TextInput(attrs={'type':"text",'class':"form-control",'placeholder':"Ingrese Correo Electrónico"}))
	password_one = forms.CharField(label="Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'class':"form-control",'placeholder':"Ingrese Contraseña"}))
	password_two = forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'class':"form-control",'placeholder':"Confirme Contraseña"}))
	
	#validar si el usuario ya existe
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username #para que valide el formulario como si fuera correcto
		raise forms.ValidationError('Nombre de usuario ya existe')
		
	#validar si ya existe el correo 
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email #para que valide el formulario como si fuera correcto
		raise forms.ValidationError('Correo ya registrado')

	#validar que el password coincida
	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Contraseña no coinciden')
			
class InscripcionesForm(forms.Form):
	cedula = forms.IntegerField(label='Cédula',widget=forms.TextInput(attrs={'type':"number",'class':"form-control",'placeholder':'Ingrese Número de Cédula'}))
	nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'type':"text", 'class':"form-control",'placeholder':'Ingrese Nombres'}))
	apellido = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'type':"text", 'class':"form-control",'placeholder':'Ingrese Apellidos'}))
	snp = forms.CharField(label='Código SNP',widget=forms.TextInput(attrs={'type':"text", 'class':"form-control",'placeholder':'Ingrese su SNP'}))
	programas_academicos= forms.ModelChoiceField(label='Seleccione la Carrera',widget=forms.Select(attrs={'class':"form-control"}), queryset=programasAcademico.objects.all())

		#validar si el número de cédula ya existe
	def clean_cedula(self):
		cedula = self.cleaned_data['cedula']
		try:
			i = inscripciones.objects.get(cedula=cedula)
		except inscripciones.DoesNotExist:
			return cedula #para que valide el formulario como si fuera correcto
		raise forms.ValidationError('Cédula ya existe')
		
		#validar si el número de cédula ya existe
	def clean_snp(self):
		snp = self.cleaned_data['snp']
		try:
			i = inscripciones.objects.get(snp=snp)
		except inscripciones.DoesNotExist:
			return snp #para que valide el formulario como si fuera correcto
		raise forms.ValidationError('Código SNP ya existe')

class ResultadoForm(forms.Form):
		programas_academicos= forms.ModelChoiceField(widget=forms.Select(attrs={'class': "form-control"}), queryset=programasAcademico.objects.all())
		Nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'type':"text", 'class':"form-control",'placeholder':'Ingrese Nombres'}))

