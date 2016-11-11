# -*- coding: utf-8 -*- 
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from univalle.administrador.forms import *
from univalle.administrador.models import *
from univalle.home.models import *
from django.core.mail import EmailMultiAlternatives #Enviamos html
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, InvalidPage#paginacion de Django
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned
import simplejson


# creamos nuestras vistas

def administrador_view(request):
	if request.user.is_authenticated():
		return render(request,'index_admin.html')
	else:
		return HttpResponseRedirect('/login')
	
def register_user_view(request):
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
			info = "Información con Datos incorrectos"
			ctx = {'form':form}
			return render(request,'registro_usuarios.html',ctx)

	ctx	= {'form':form}
	return render(request,'registro_usuarios.html', ctx)
	
def listar_usuario_view(request):
	if request.user.is_authenticated():
		return render(request,'listar_usuarios.html',ctx)
	else:
		return HttpResponseRedirect('/login')
		
def register_inscripcion_view(request):
	mensaje=""
	llamarMensaje=""
	form = RegistroInscripcionesForm()
	if request.user.is_authenticated():
		if request.method == "POST":
			form = RegistroInscripcionesForm(request.POST)
			if form.is_valid():
				cedula = form.cleaned_data['cedula']
				nombre = form.cleaned_data['nombre']
				apellido = form.cleaned_data['apellido']
				snp = form.cleaned_data['snp']
				programa = str(form.cleaned_data['programas_academicos'])
				try:
					i = inscripciones.objects.get(cedula=cedula)
				except inscripciones.DoesNotExist:
					i = inscripciones() #creo una instancia de la clase inscripcion
					
					i.cedula = cedula
					i.nombre = nombre
					i.apellido = apellido
					i.snp = snp
					i.carrera = programa	
					
					i.save() #guardar inscripcion
					llamarMensaje= "Registro"
					mensaje= "Registro Satisfactorio!!!!!!"
					form = RegistroInscripcionesForm()
				else:
					llamarMensaje="NoRegistro"
					mensaje="Ya existe un usuario con este número de Cédula"
			else:
				mensaje = "Datos erróneos"
				
		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje}
		return render(request,'registro_inscripciones.html',ctx)
	else:
		return HttpResponseRedirect('/login')
		
def editar_inscripcion_view(request,cedula=None):
	mensaje = ""
	llamarMensaje=""
	i = inscripciones.objects.get(cedula=cedula)
	if request.user.is_authenticated():
		if request.method == "POST":
			form = EditarInscripcionesForm(request.POST)
			if form.is_valid():
				cedula = form.cleaned_data['cedula']
				nombre = form.cleaned_data['nombre']
				apellido = form.cleaned_data['apellido']
				snp = form.cleaned_data['snp']
				programa = str(form.cleaned_data['programas_academicos'])
				
				i = inscripciones() #creo una instancia de la clase inscripcion
				
				i.cedula = cedula
				i.nombre = nombre
				i.apellido = apellido
				i.snp = snp
				i.carrera = programa
				
				i.save() #guardar inscripcion
				llamarMensaje= "Registro"
				mensaje= "Actualización Satisfactoria!!!!!!"
			else:
				mensaje = "Datos erróneos"

		if request.method == "GET":
			form = EditarInscripcionesForm(initial={
				'cedula': i.cedula,
				'nombre': i.nombre,
				'apellido': i.apellido,
				'snp': i.snp,
				'programas_academicos': i.carrera,
			})
		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje}
		return render(request,'editar_inscripciones.html',ctx)
	else:
		return HttpResponseRedirect('/login')

def listar_inscripciones_view(request,pagina):
	#Metodo POST para eliminar inscripcion
	if request.user.is_authenticated():
		if request.method=="POST":
			if "programa_id" in request.POST:
				try:
					cedula = request.POST['programa_id']
					i = inscripciones.objects.get(cedula=cedula)
					mensaje = {"status":"True","programa_id":i.cedula}
					i.delete() # Eliminamos objeto de la base de datos
					return HttpResponse(simplejson.dumps(mensaje),content_type ='application/json')
				except:
					mensaje = {"status":"False"}
					return HttpResponse(simplejson.dumps(mensaje),content_type ='application/json')
					
	#Metodo  para listar inscripciones				
		lista_inscrip = inscripciones.objects.filter(status=True)
		paginator = Paginator(lista_inscrip,7)
		try:
			page = int(pagina)
		except:
			page = 1
		try:
			inscripcion = paginator.page(page)
		except:
			inscripcion = paginator.page(paginator.num_pages)
			
		ctx = {'inscripcion':inscripcion}
		return render(request, 'listar_inscripciones.html',ctx)
	else:
		return HttpResponseRedirect('/login')

def register_carrera_view(request):
	mensaje=""
	llamarMensaje=""
	form = CarreraForm()
	if request.user.is_authenticated():
		if request.method == "POST":
			form = CarreraForm(request.POST)
			if form.is_valid():
				codigo = form.cleaned_data['codigo']
				nombre = form.cleaned_data['nombre']
				try:
					p = programasAcademico.objects.get(codigo=codigo)
				except programasAcademico.DoesNotExist:
					p = programasAcademico() #creo una instancia de la clase programaAcademico
					p.codigo = codigo
					p.nombre = nombre
					p.save() #guardar programa
					llamarMensaje= "Registro"
					mensaje= "Registro Satisfactorio!!!!!!"
					form = CarreraForm()
				else:
					llamarMensaje="NoRegistro"
					mensaje="Código de carrera ya existe"
			else:
				mensaje = "Datos erróneos"

		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje}
		return render(request,'registro_carreras.html',ctx)
	else:
		return HttpResponseRedirect('/login')

def editar_carrera_view(request,codigo=None):
	mensaje = ""
	llamarMensaje=""
	p = programasAcademico.objects.get(codigo=codigo)
	if request.user.is_authenticated():
		if request.method == "POST":
			form = EditarCarreraForm(request.POST)
			if form.is_valid():
				codigo = form.cleaned_data['codigo']
				nombre = form.cleaned_data['nombre']
				p = programasAcademico() #creo una instancia de la clase inscripcion
				p.codigo = codigo
				p.nombre = nombre
				p.save() #guardar inscripcion
				llamarMensaje= "Registro"
				mensaje= "Actualización Satisfactoria!!!!!!"
			else:
				mensaje = "Datos erróneos"

		if request.method == "GET":
			form = EditarCarreraForm(initial={
				'codigo': p.codigo,
				'nombre': p.nombre,
			})
		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje}
		return render(request,'editar_carreras.html',ctx)
	else:
		return HttpResponseRedirect('/login')

def listar_carreras_view(request,pagina):
	#Metodo POST para eliminar programa academico
	if request.user.is_authenticated():
		if request.method=="POST":
			if "programa_id" in request.POST:
				try:
					codigo = request.POST['programa_id']
					p = programasAcademico.objects.get(codigo=codigo)
					mensaje = {"status":"True","programa_id":p.codigo}
					p.delete() # Eliminamos objeto de la base de datos
					return HttpResponse(simplejson.dumps(mensaje),content_type ='application/json')
				except:
					mensaje = {"status":"False"}
					return HttpResponse(simplejson.dumps(mensaje),content_type ='application/json')
					
	#Metodo  para listar programas academicos				
		lista_carr = programasAcademico.objects.filter(status=True)
		paginator = Paginator(lista_carr,7)
		try:
			page = int(pagina)
		except:
			page = 1
		try:
			carreras = paginator.page(page)
		except:
			carreras = paginator.page(paginator.num_pages)
			
		ctx = {'carreras':carreras}
		return render(request, 'listar_carreras.html',ctx)
	else:
		return HttpResponseRedirect('/login')
		
