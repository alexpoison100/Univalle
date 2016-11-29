# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.template import RequestContext
from univalle.home.forms import *
from univalle.home.models import *
from django.core.mail import EmailMultiAlternatives #Enviamos html
from django.contrib.auth import login, logout, authenticate 
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage#paginacion de Django
from django.contrib.auth.models import User
import itertools#contador indice de la tabla

# creamos nuestras vistas

def index_view(request):
	#muestra el index pero con el formulario de contacto
	info_enviado = False #definir si se envio la info
	nombre = ""
	correo = ""
	asunto = ""
	mensaje = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			nombre = formulario.cleaned_data['Nombre']
			correo = formulario.cleaned_data['Correo']
			asunto = formulario.cleaned_data['Asunto']
			mensaje = formulario.cleaned_data['Mensaje']

			#configuracion enviando mensaje via gmail
			to_admin = 'alexpoison100@gmail.com'
			html_content ="<b>Informacion recibida de:</b> %s <br><b>Asunto:</b> %s<br><br><b>***Mensaje***</b><br><br>%s"%(correo,asunto,mensaje)
			msg = EmailMultiAlternatives("Correo de Contacto",html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')#definimos el contenido como HTML
			msg.send()#Enviamos el correo
		
	else:
		formulario = ContactForm()
	ctx = {'form':formulario,'info_enviado':info_enviado}
	return render(request,'index.html',ctx)

def about_view(request):
	mensaje ="Esto es un mensaje desde mi vista"
	ctx = {'msg':mensaje}
	return render(request,'about.html',ctx)

def login_view(request):
	mensaje=""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')#lo direccionamos a la raiz si no esta autenticado
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['Usuario']
				password = form.cleaned_data['Contrasena']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje="Usuario y/o password incorrecto"
			else:
					mensaje="Falta llenar campos vacios"
		form = LoginForm()
		ctx = {'form':form, 'mensaje':mensaje}
		return render(request,'login.html',ctx)
	 
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def register_view(request):
	info="inicializado"
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=username, email=email, password=password_one)
			u.save()#guarda el usuario
			return render(request,'thanks_register.html')
		else:
			info = "Datos incorrectos"
			ctx = {'form':form}
			return render(request,'registro.html',ctx)

	ctx	= {'form':form}
	return render(request,'registro.html', ctx)
	
def resultados_view(request):
	if request.user.is_authenticated():
		mensaje =""
		programas_academicos=""
		form = ResultadoForm()
		
		if request.method == "POST":
			form = ResultadoForm(request.POST)
			
			if form.is_valid():
				programas_academicos = str(form.cleaned_data['programas_academicos'])
				form = ResultadoForm(request.POST)
				return HttpResponseRedirect('/listar_admitidos/pagina/1/programa/%s' % programas_academicos)
			else:
				mensaje = "No ha seleccionado ninguna Carrera"
				ctx = {'form':form}
				return render(request,'resultados.html',ctx)
		form = ResultadoForm()
		ctx = {'form':form, 'mensaje':mensaje}
		return render(request,'resultados.html',ctx)
	else:
		return HttpResponseRedirect('/login')	
		
	
def add_inscripciones_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			formulario = InscripcionesForm(request.POST)
			info = "Inicializando"
			
			if formulario.is_valid():
				cedula = formulario.cleaned_data['cedula']
				nombre = formulario.cleaned_data['nombre']
				apellido = formulario.cleaned_data['apellido']
				snp = formulario.cleaned_data['snp']
				ref_pago = formulario.cleaned_data['ref_pago']					#ojoooooooooooooooooooo falta consultar al web service este  pago 
				programa = str(formulario.cleaned_data['programas_academicos'])
			
				i = inscripciones() #creo una instancia de la clase inscripcion
				
				i.cedula = cedula
				i.nombre = nombre
				i.apellido = apellido
				i.snp = snp
				i.ref_pago = ref_pago
				i.carrera = programa
				
				i.save() #guardar inscripcion
				
				a = listado_admitidos() #creo una instancia de la clase lista
				
				a.cedula = cedula
				a.nombre = nombre
				a.apellido = apellido
				a.puntaje = 320                          #ojoooooooooooooooooooo falta consultar al web service este  puntaje
				a.carrera = programa
				
				a.save() #guardar listado
				info = "Inscripción Satisfactoria!!!!!!"
				formulario = InscripcionesForm()
			else:
				info = "Informacion con datos incorrectos"
			form = InscripcionesForm()
			ctx = {'form':formulario, 'informacion':info}
			return render(request,'inscripciones.html',ctx)

		else:
			formulario = InscripcionesForm()
		ctx = {'form':formulario}
		return render(request,'inscripciones.html',ctx)
	else:
		return HttpResponseRedirect('/')

def listar_admitidos_view(request,pagina,carrera=None):
	iterator = itertools.count(1)#me genera un contador para el indice de la tabla
	if request.user.is_authenticated():
	#Metodo  para listar inscripciones
		#consulta por carrera, de mayor a menor puntaje y un cupo para 3
		lista_admitidos = listado_admitidos.objects.filter(carrera=carrera).order_by('-puntaje')[:3]
		paginator = Paginator(lista_admitidos,20)
		try:
			page = int(pagina)
		except:
			page = 1
		try:
			admitidos = paginator.page(page)
		except:
			admitidos = paginator.page(paginator.num_pages)
			
		ctx = {'admitidos':admitidos,'iterator':iterator,'carrera':carrera}
		return render(request, 'listar_admitidos.html',ctx)
	else:
		return HttpResponseRedirect('/login')	