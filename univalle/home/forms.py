# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.auth.models import User
from univalle.home.models import *
#from univalle.home.passw import *

class ContactForm(forms.Form):
	Nombre	= forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'required': True,'type':"text",'class':"form-control",'placeholder':'Ingrese Nombre'}))
	Correo	= forms.EmailField(label="Correo Electrónico",widget=forms.TextInput(attrs={'required': True,'type':"email",'class':"form-control",'placeholder':"Ingrese Correo Electrónico"}))
	Asunto	= forms.CharField(label="Asunto",widget=forms.TextInput(attrs={'required': True,'type':"text",'class':"form-control",'placeholder':'Ingrese Asunto'}))
	Mensaje	= forms.CharField(label="Mensaje",widget=forms.Textarea(attrs={'required': True,'class':"form-control",'rows':5,'placeholder':'Ingrese Mensaje'}))

class LoginForm(forms.Form):
	Usuario = forms.CharField(widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Usuario'}))
	Contrasena = forms.CharField(label="Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':'Ingrese Contraseña'}))

class RegisterForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':"Ingrese Usuario"}))
	email = forms.EmailField(label="Correo Electrónico",widget=forms.TextInput(attrs={'type':"text",'class':"form-control",'placeholder':"Ingrese Correo Electrónico"}))
	password_one = forms.CharField(label="Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':"Ingrese Contraseña"}))
	password_two = forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'trequired': True,'class':"form-control",'placeholder':"Confirme Contraseña"}))
	
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

	#validar que el password coincida y tenga mínimo 8 caracteres, minisculas y mayusculas
	def clean_password_old(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		espacio=False
		mayuscula=False #variable para identificar letras mayúsculas
		minuscula=False #variable para contar identificar letras minúsculas
		numeros=False
        
		for carac in password_one :
			if carac.isspace()==True: #Saber si el caracter es un espacio
				espacio=True #si encuentra un espacio se cambia el valor user
			if carac.isupper()== True: #saber si hay mayuscula
				mayuscula=True #acumulador o contador de mayusculas
			if carac.islower()== True: #saber si hay minúsculas
				minuscula=True #acumulador o contador de minúsculas
			if carac.isdigit()== True: #saber si hay números
				numeros=True #acumulador o contador de numeros
                    
		if espacio==True:
			raise forms.ValidationError('La contraseña no puede contener espacios en blanco')
			
		if len(password_one) < 5 :
			raise forms.ValidationError('La contraseña debe tener mínimo 5 caracteres')

		if mayuscula == True and minuscula ==True and numeros == True :
			pass
		else:
			raise forms.ValidationError('La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas y números')
			
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Contraseña no coinciden')
			
class InscripcionesForm(forms.Form):
	cedula = forms.IntegerField(label='Cédula',widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese su Número de Cédula'}))
	nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese su Nombre Completo'}))
	apellido = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese sus Apellidos'}))
	snp = forms.CharField(label='Número de Registro ICFES',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese su número de Registro ICFES'}))
	ref_pago = forms.IntegerField(label='Referencia de Pago',widget=forms.TextInput(attrs={'required': True,'type':"number", 'class':"form-control",'placeholder':'Ingrese referencia de pago'}))
	programas_academicos= forms.ModelChoiceField(label='Seleccione la Carrera',widget=forms.Select(attrs={'required': True,'class':"form-control"}), queryset=programasAcademico.objects.all())

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
		
class EditarInscripcionesForm(forms.Form):
	cedula = forms.IntegerField(label='Cédula',widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese Número de Cédula'}))
	nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Nombres'}))
	apellido = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Apellidos'}))
	snp = forms.CharField(label='Número de Registro ICFES',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese su número de Registro ICFES'}))
	ref_pago = forms.IntegerField(label='Referencia de Pago',widget=forms.TextInput(attrs={'required': True,'type':"number", 'class':"form-control",'placeholder':'Ingrese referencia de pago'}))
	programas_academicos= forms.ModelChoiceField(label='Seleccione la Carrera',widget=forms.Select(attrs={'required': True,'class':"form-control"}), queryset=programasAcademico.objects.all())

class ResultadoForm(forms.Form):
		programas_academicos= forms.ModelChoiceField(widget=forms.Select(attrs={'required': True,'class': "form-control"}), queryset=programasAcademico.objects.all())

