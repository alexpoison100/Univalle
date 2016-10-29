# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.auth.models import User
from univalle.administrador.models import *
from univalle.home.models import *



class RegisterForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':"Ingrese Usuario"}))
	email = forms.EmailField(label="Correo Electrónico",widget=forms.TextInput(attrs={'type':"text",'class':"form-control",'placeholder':"Ingrese Correo Electrónico"}))
	password_one = forms.CharField(label="Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':"Ingrese Contraseña"}))
	password_two = forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':"Confirme Contraseña"}))
	
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
			
class CarreraForm(forms.Form):
    codigo = forms.IntegerField(label="Código",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese Código'}))
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'required': True,'type':"text",'class':"form-control",'placeholder':'Ingrese Nombre'}))

class EditarCarreraForm(forms.Form):
    codigo = forms.IntegerField(label="Código",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese Código','readonly':"readonly"}))
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'required': True,'type':"text",'class':"form-control",'placeholder':'Ingrese Nombre'}))

