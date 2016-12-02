# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.auth.models import User
from univalle.administrador.models import *
from univalle.home.models import *
import requests

class CorreoForm(forms.Form):
	correo	= forms.EmailField(label="Correo Electrónico",widget=forms.TextInput(attrs={'required': True,'type':"email",'class':"form-control",'placeholder':"Para:"}))
	asunto	= forms.CharField(label="Asunto",widget=forms.TextInput(attrs={'required': True,'type':"text",'class':"form-control",'placeholder':'Asunto:'}))
	texto	= forms.CharField(label="Mensaje",widget=forms.Textarea(attrs={'required': True,'class':"form-control", 'rows':6, 'placeholder':'Ingrese Mensaje'}))

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
    lectura_critica = forms.FloatField(label="Lectura crítica",widget=forms.TextInput(attrs={'required': True,'min_value':0.01,'max_value':1.00,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    matematicas = forms.FloatField(label="Matemáticas",widget=forms.TextInput(attrs={'required': True,'min_value':0.01,'max_value':1.00,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    sociales = forms.FloatField(label="Sociales",widget=forms.TextInput(attrs={'required': True,'min_value':0.01,'max_value':1.00,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    naturales = forms.FloatField(label="Naturales",widget=forms.TextInput(attrs={'required': True,'min_value':0.01,'max_value':1.00,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    ingles = forms.FloatField(label="Inglés",widget=forms.TextInput(attrs={'required': True,'min_value':0.01,'max_value':1.00,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    razonamiento_cuantitativo = forms.FloatField(label="Razonamiento cuantitativo",widget=forms.TextInput(attrs={'required': True,'min_value':0.01,'max_value':1.00,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    competencias_ciudadanas = forms.FloatField(label="Competencias ciudadanas",widget=forms.TextInput(attrs={'required': True,'min_value':0.01,'max_value':1.00,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    puntaje_min = forms.IntegerField(label="Puntaje mínimo",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese Puntaje mínimo de la carrera'}))
    info	= forms.CharField(label="Información",widget=forms.Textarea(attrs={'required': True,'class':"form-control",'rows':5,'placeholder':'Ingrese Información de la carrera'}))
	
class EditarCarreraForm(forms.Form):
    codigo = forms.IntegerField(label="Código",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese Código','readonly':"readonly"}))
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'required': True,'type':"text",'class':"form-control",'placeholder':'Ingrese Nombre'}))
    lectura_critica = forms.FloatField(label="Lectura crítica",widget=forms.TextInput(attrs={'required': True,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    matematicas = forms.FloatField(label="Matemáticas",widget=forms.TextInput(attrs={'required': True,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    sociales = forms.FloatField(label="Sociales",widget=forms.TextInput(attrs={'required': True,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    naturales = forms.FloatField(label="Naturales",widget=forms.TextInput(attrs={'required': True,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    ingles = forms.FloatField(label="Inglés",widget=forms.TextInput(attrs={'required': True,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    razonamiento_cuantitativo = forms.FloatField(label="Razonamiento cuantitativo",widget=forms.TextInput(attrs={'required': True,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    competencias_ciudadanas = forms.FloatField(label="Competencias ciudadanas",widget=forms.TextInput(attrs={'required': True,'step': "0.01",'type':"number",'class':"form-control",'placeholder':'Ingrese Ponderación'}))
    puntaje_min = forms.IntegerField(label="Puntaje mínimo",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese Puntaje mínimo de la carrera'}))
    info	= forms.CharField(label="Información",widget=forms.Textarea(attrs={'required': True,'class':"form-control",'rows':5,'placeholder':'Ingrese Información de la carrera'}))

class RegistroInscripcionesForm(forms.Form):
	cedula = forms.IntegerField(label='Cédula',widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese Número de Cédula'}))
	nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Nombres'}))
	apellido = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Apellidos'}))
	snp = forms.CharField(label='Número de Registro ICFES',widget=forms.TextInput(attrs={'id':'snp','required': True,'type':"text", 'onChange':'icfes()','class':"form-control",'placeholder':'Ingrese su número de Registro ICFES'}))
	lectura_critica = forms.IntegerField(label="Lectura crítica",widget=forms.TextInput(attrs={'id':'lectura_critica','required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Lectura crítica','readonly':"readonly"}))
	matematicas = forms.IntegerField(label="Matemáticas",widget=forms.TextInput(attrs={'id':'matematicas','required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Matemáticas','readonly':"readonly"}))
	sociales = forms.IntegerField(label="Sociales",widget=forms.TextInput(attrs={'id':'sociales','required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Sociales','readonly':"readonly"}))
	naturales = forms.IntegerField(label="Naturales",widget=forms.TextInput(attrs={'id':'naturales','required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Naturales','readonly':"readonly"}))
	ingles = forms.IntegerField(label="Inglés",widget=forms.TextInput(attrs={'id':'ingles','required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Inglés','readonly':"readonly"}))
	razonamiento_cuantitativo = forms.IntegerField(label="Razonamiento cuantitativo",widget=forms.TextInput(attrs={'id':'razonamiento_cuantitativo','required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Razonamiento cuantitativo','readonly':"readonly"}))
	competencias_ciudadanas = forms.IntegerField(label="Competencias ciudadanas",widget=forms.TextInput(attrs={'id':'competencias_ciudadanas','required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Competencias ciudadanas','readonly':"readonly"}))
	colegio = forms.CharField(label='Colegio',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Nombre del Colegio'}))
	ref_pago = forms.IntegerField(label='Referencia de Pago',widget=forms.TextInput(attrs={'required': True,'type':"number", 'class':"form-control",'placeholder':'Ingrese referencia de pago'}))
	programas_academicos= forms.ModelChoiceField(label='Seleccione la Carrera',widget=forms.Select(attrs={'required': True,'class':"form-control"}), queryset=programasAcademico.objects.all().order_by('nombre'))
	
	def clean_snp(self):
		snp = self.cleaned_data['snp']
		if snp:
			icfes = requests.get('https://morning-brushlands-79611.herokuapp.com/v1/resultados/?codigo=%s&format=json' % snp)
			icfes_json = icfes.json()
			if icfes_json:
				return snp
			else:
				raise forms.ValidationError('Número de Registro No existe')
				
	#validar si el numero de pago es valido en el microservicio			
	def clean_ref_pago(self):
		ref_pago = self.cleaned_data['ref_pago']
		if ref_pago:
			respuesta = requests.get('http://ws-bank-julianrico.c9users.io/rest/consignacion/?cedula=%s&format=json' % ref_pago)
			respuesta_json = respuesta.json()
			if respuesta_json:
				return ref_pago
			else:
				raise forms.ValidationError('Número de Pago No existe')

class EditarInscripcionesForm(forms.Form):
	cedula = forms.IntegerField(label='Cédula',widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Ingrese Número de Cédula','readonly':"readonly"}))
	nombre = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Nombres'}))
	apellido = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Apellidos'}))
	snp = forms.CharField(label='Número de Registro ICFES',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese su número de Registro ICFES'}))
	lectura_critica = forms.IntegerField(label="Lectura crítica",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Lectura crítica','readonly':"readonly"}))
	matematicas = forms.IntegerField(label="Matemáticas",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Matemáticas','readonly':"readonly"}))
	sociales = forms.IntegerField(label="Sociales",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Sociales','readonly':"readonly"}))
	naturales = forms.IntegerField(label="Naturales",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Naturales','readonly':"readonly"}))
	ingles = forms.IntegerField(label="Inglés",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Inglés','readonly':"readonly"}))
	razonamiento_cuantitativo = forms.IntegerField(label="Razonamiento cuantitativo",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Razonamiento cuantitativo','readonly':"readonly"}))
	competencias_ciudadanas = forms.IntegerField(label="Competencias ciudadanas",widget=forms.TextInput(attrs={'required': True,'type':"number",'class':"form-control",'placeholder':'Resultado de Competencias ciudadanas','readonly':"readonly"}))
	ref_pago = forms.IntegerField(label='Referencia de Pago',widget=forms.TextInput(attrs={'required': True,'type':"number", 'class':"form-control",'placeholder':'Ingrese referencia de pago'}))
	colegio = forms.CharField(label='Colegio',widget=forms.TextInput(attrs={'required': True,'type':"text", 'class':"form-control",'placeholder':'Ingrese Nombre del Colegio'}))
	programas_academicos= forms.ModelChoiceField(label='Seleccione la Carrera',widget=forms.Select(attrs={'nombre':'demo-cs-multiselect','required': True,'class':"form-control"}), queryset=programasAcademico.objects.all().order_by('nombre'))

	def clean_snp(self):
		snp = self.cleaned_data['snp']
		if snp:
			icfes = requests.get('https://morning-brushlands-79611.herokuapp.com/v1/resultados/?codigo=%s&format=json' % snp)
			icfes_json = icfes.json()
			if icfes_json:
				return snp
			else:
				raise forms.ValidationError('Número de Registro No existe')
	
	#validar si el numero de pago es valido en el microservicio			
	def clean_ref_pago(self):
		ref_pago = self.cleaned_data['ref_pago']
		if ref_pago:
			respuesta = requests.get('http://ws-bank-julianrico.c9users.io/rest/consignacion/?cedula=%s&format=json' % ref_pago)
			respuesta_json = respuesta.json()
			if respuesta_json:
				return ref_pago
			else:
				raise forms.ValidationError('Número de Pago No existe')
				
class EditarPasswordForm(forms.Form):
	password_actual = forms.CharField(label="Contraseña Actual",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':"Ingrese Contraseña Actual"}))
	password_one = forms.CharField(label="Nueva Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':"Ingrese Nueva Contraseña"}))
	password_two = forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput(render_value=False, attrs={'required': True,'class':"form-control",'placeholder':"Confirme Nueva Contraseña"}))
