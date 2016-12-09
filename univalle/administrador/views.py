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
from django.contrib.auth.hashers import check_password#libreria para chequear password actual
import itertools#contador indice de la tabla
import requests

# creamos nuestras vistas
def icfes (request):
    if request.method == "POST":
        snp = request.POST['snp']
        url = "https://morning-brushlands-79611.herokuapp.com/v1/resultados/?codigo=" + snp + "&format=json"
        webservice = requests.get(url, verify=True)
        return HttpResponse(webservice)
        
def administrador_view(request):
	#muestra el index pero con el formulario de contacto
	nombre = ""
	correo = ""
	asunto = ""
	texto = ""
	mensaje=""
	llamarMensaje=""
	totalUsuarios= User.objects.count()#cuenta la cantidad de usuarios registrados
	totalInscripciones= inscripciones.objects.count()#cuenta la cantidad de inscripciones
	totalCarreras= programasAcademico.objects.count()#cuenta la cantidad de programas academicos
	form = CorreoForm()
	
	if request.user.is_authenticated():
		if request.method == "POST":
			form = CorreoForm(request.POST)
			if form.is_valid():
				llamarMensaje= "Registro"
				mensaje= "Mensaje Enviado!!!!!!"
				correo = form.cleaned_data['correo']
				asunto = form.cleaned_data['asunto']
				texto = form.cleaned_data['texto']
				
				#configuracion enviando mensaje via gmail
				to_admin = correo
				html_content ="<b>Asunto:</b> %s<br><br><b>Mensaje:</b><br><br>%s"%(asunto,texto)
				msg = EmailMultiAlternatives("Correo de Contacto",html_content,'from@server.com',[to_admin])
				msg.attach_alternative(html_content,'text/html')#definimos el contenido como HTML
				msg.send()#Enviamos el correo
				form = CorreoForm()
			else:
				llamarMensaje= "NoRegistro"
				mensaje= "Mensaje No Enviado!!!!!!"
				form = CorreoForm()
		ctx = {'form':form,'mensaje':mensaje, 'llamarMensaje':llamarMensaje, 'totalCarreras':totalCarreras,'totalUsuarios':totalUsuarios, 'totalInscripciones':totalInscripciones}
		return render(request,'index_admin.html',ctx)
	else:
		return HttpResponseRedirect('/login')

def register_user_view(request):
	mensaje=""
	llamarMensaje=""
	info=""
	form = RegistroUsuarioForm()
	if request.user.is_authenticated():
		if request.method == "POST":
			form = RegistroUsuarioForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				email = form.cleaned_data['email']
				password_one = form.cleaned_data['password_one']
				password_two = form.cleaned_data['password_two']
			
				u = User.objects.create_user(username=username, email=email, password=password_one)
				u.save()#guarda el usuario
				llamarMensaje= "Registro"
				mensaje= "Registro Satisfactorio!!!!!!"
				form = RegistroUsuarioForm()

			else:
				llamarMensaje="NoRegistro"
				mensaje = "DATOS INCORRECTOS!!!!!!"
		ctx = {'form':form,'info':info, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje}
		return render(request,'registro_usuarios.html',ctx)
	else:
		return HttpResponseRedirect('/login')

def editar_usuario_view(request,pk=None):
	mensaje = ""
	llamarMensaje=""
	info=""
	u = User.objects.get(pk=pk)
	if request.user.is_authenticated():
		if request.method == "POST":
			form = EditarUsuarioForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				email = form.cleaned_data['email']
				
				u = User()
				u.pk = pk
				u.username = username
				u.email = email
				u.save() #guardar usuario
				llamarMensaje= "Registro"
				mensaje= "Actualización Satisfactoria!!!!!!"
			else:
				llamarMensaje="NoRegistro"
				mensaje = "DATOS INCORRECTOS!!!!!!"
		#se carga el formulario con los datos del usuario a editar		
		if request.method == "GET":
			form = EditarUsuarioForm(initial={
				'username': u.username,
				'email': u.email,
			})
		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje,'info':info}
		return render(request,'editar_usuarios.html',ctx)
	else:
		return HttpResponseRedirect('/login')
	
def listar_usuario_view(request,pagina):
	#Metodo POST para eliminar usuario
	if request.user.is_authenticated():
		if request.method=="POST":
			if "programa_id" in request.POST:
				try:
					pk = request.POST['programa_id']
					u = User.objects.get(pk=pk)
					mensaje = {"status":"True","programa_id":u.pk}
					u.delete() # Eliminamos objeto de la base de datos
					return HttpResponse(simplejson.dumps(mensaje),content_type ='application/json')
				except:
					mensaje = {"status":"False"}
					return HttpResponse(simplejson.dumps(mensaje),content_type ='application/json')
					
	#Metodo  para listar usuarios				
		lista_user = User.objects.filter()
		paginator = Paginator(lista_user,7)
		try:
			page = int(pagina)
		except:
			page = 1
		try:
			usuarios = paginator.page(page)
		except:
			usuarios = paginator.page(paginator.num_pages)
			
		ctx = {'usuarios':usuarios}
		return render(request, 'listar_usuarios.html',ctx)
	else:
		return HttpResponseRedirect('/login')
		
def register_inscripcion_view(request):
	mensaje=""
	llamarMensaje=""
	info=""
	form = RegistroInscripcionesForm()
	if request.user.is_authenticated():
		if request.method == "POST":
			formulario = RegistroInscripcionesForm(request.POST)
			info = "Inicializando"
			
			if formulario.is_valid():
				cedula = formulario.cleaned_data['cedula']
				nombre = formulario.cleaned_data['nombre']
				apellido = formulario.cleaned_data['apellido']
				snp = formulario.cleaned_data['snp']
				lectura_critica= formulario.cleaned_data['lectura_critica']
				matematicas= formulario.cleaned_data['matematicas']
				sociales= formulario.cleaned_data['sociales']
				naturales= formulario.cleaned_data['naturales']
				ingles= formulario.cleaned_data['ingles']
				razonamiento_cuantitativo= formulario.cleaned_data['razonamiento_cuantitativo']
				competencias_ciudadanas= formulario.cleaned_data['competencias_ciudadanas']
				colegio = formulario.cleaned_data['colegio']
				ref_pago = formulario.cleaned_data['ref_pago']
				programa = str(formulario.cleaned_data['programas_academicos'])

				i = inscripciones()
				
				i.cedula = cedula
				i.nombre = nombre
				i.apellido = apellido
				i.snp = snp
				i.lectura_critica = lectura_critica
				i.matematicas = matematicas
				i.sociales = sociales
				i.naturales = naturales
				i.ingles = ingles
				i.razonamiento_cuantitativo = razonamiento_cuantitativo
				i.competencias_ciudadanas = competencias_ciudadanas
				i.colegio = colegio
				i.ref_pago = ref_pago
				i.carrera = programa
				
				i.save() #guardar inscripcion
				#Consulta de los ponderados de cada materia
				try:
					p = programasAcademico.objects.get(nombre=programa)
				except programasAcademico.DoesNotExist:
					info = "Programa No existe"
				else:
					pl = p.lectura_critica
					pm = p.matematicas
					ps = p.sociales
					pn = p.naturales
					pi = p.ingles
					pr = p.razonamiento_cuantitativo
					pc = p.competencias_ciudadanas
				#Aqui se multiplica cada uno de los resultados de cada prueba por la ponderación que el programa académico 
				puntaje = float((lectura_critica) * (pl)) + float((matematicas) * (pm)) + float((sociales) * (ps)) + float((naturales) * (pn)) + float((ingles) * (pi)) + float((razonamiento_cuantitativo) * (pr)) + float((competencias_ciudadanas) * (pc))
				
				#Guardo datos para generar la lista de admitidos
				a = lista_admitidos() #creo una instancia de la clase lista
				
				a.cedula = cedula
				a.nombre = nombre
				a.apellido = apellido
				a.puntaje = puntaje                         
				a.carrera = programa
				
				a.save() #guardar listado
				llamarMensaje= "Registro"
				mensaje= "Registro Satisfactorio!!!!!!"
				formulario = RegistroInscripcionesForm()
			else:
				llamarMensaje= "NoRegistro"
				mensaje= "DATOS INCORRECTOS!!!!!!"
			form = RegistroInscripcionesForm()
			ctx = {'form':formulario, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje,'info':info}
			return render(request,'registro_inscripciones.html',ctx)

		else:
			formulario = RegistroInscripcionesForm()
		ctx = {'form':formulario, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje}
		return render(request,'registro_inscripciones.html',ctx)
	else:
		return HttpResponseRedirect('/login')
		
def editar_inscripcion_view(request,cedula=None):
	mensaje = ""
	llamarMensaje=""
	info=""
	i = inscripciones.objects.get(cedula=cedula)
	a = lista_admitidos.objects.get(cedula=cedula)
	if request.user.is_authenticated():
		if request.method == "POST":
			form = EditarInscripcionesForm(request.POST)
			if form.is_valid():
				cedula = form.cleaned_data['cedula']
				nombre = form.cleaned_data['nombre']
				apellido = form.cleaned_data['apellido']
				snp = form.cleaned_data['snp']
				lectura_critica= form.cleaned_data['lectura_critica']
				matematicas= form.cleaned_data['matematicas']
				sociales= form.cleaned_data['sociales']
				naturales= form.cleaned_data['naturales']
				ingles= form.cleaned_data['ingles']
				razonamiento_cuantitativo= form.cleaned_data['razonamiento_cuantitativo']
				competencias_ciudadanas= form.cleaned_data['competencias_ciudadanas']
				colegio = form.cleaned_data['colegio']
				ref_pago = form.cleaned_data['ref_pago']
				programa = str(form.cleaned_data['programas_academicos'])
				
				i = inscripciones() #creo una instancia de la clase inscripcion
				
				i.cedula = cedula
				i.nombre = nombre
				i.apellido = apellido
				i.snp = snp
				i.lectura_critica = lectura_critica
				i.matematicas = matematicas
				i.sociales = sociales
				i.naturales = naturales
				i.ingles = ingles
				i.razonamiento_cuantitativo = razonamiento_cuantitativo
				i.competencias_ciudadanas = competencias_ciudadanas
				i.colegio = colegio
				i.ref_pago = ref_pago
				i.carrera = programa

				i.save() #guardar inscripcion
				
				#Consulta de los ponderados de cada materia
				try:
					p = programasAcademico.objects.get(nombre=programa)
				except programasAcademico.DoesNotExist:
					info = "Programa No existe"
				else:
					pl = p.lectura_critica
					pm = p.matematicas
					ps = p.sociales
					pn = p.naturales
					pi = p.ingles
					pr = p.razonamiento_cuantitativo
					pc = p.competencias_ciudadanas
				#Aqui se multiplica cada uno de los resultados de cada prueba por la ponderación que el programa académico 
				puntaje = float((lectura_critica) * (pl)) + float((matematicas) * (pm)) + float((sociales) * (ps)) + float((naturales) * (pn)) + float((ingles) * (pi)) + float((razonamiento_cuantitativo) * (pr)) + float((competencias_ciudadanas) * (pc))
				
				#Guardo datos para generar la lista de admitidos
				a = lista_admitidos() #creo una instancia de la clase lista
				
				a.cedula = cedula
				a.nombre = nombre
				a.apellido = apellido
				a.puntaje = puntaje                          
				a.carrera = programa
				
				a.save() #guardar listado
				
				llamarMensaje= "Registro"
				mensaje= "Actualización Satisfactoria!!!!!!"
			else:
				llamarMensaje= "NoRegistro"
				mensaje= "DATOS INCORRECTOS!!!!!!"

		if request.method == "GET":
			form = EditarInscripcionesForm(initial={
				'cedula': i.cedula,
				'nombre': i.nombre,
				'apellido': i.apellido,
				'snp': i.snp,
				'lectura_critica': i.lectura_critica,
				'matematicas': i.matematicas,
				'sociales': i.sociales,
				'naturales': i.naturales,
				'ingles': i.ingles,
				'razonamiento_cuantitativo': i.razonamiento_cuantitativo,
				'competencias_ciudadanas': i.competencias_ciudadanas,
				'colegio': i.colegio,
				'ref_pago':i.ref_pago,
				'programas_academicos': [o for o in i.carrera],
			})
		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje,'info':info}
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
		paginator = Paginator(lista_inscrip,10)
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
				lectura_critica = form.cleaned_data['lectura_critica']
				matematicas = form.cleaned_data['matematicas']
				sociales = form.cleaned_data['sociales']
				naturales = form.cleaned_data['naturales']
				ingles = form.cleaned_data['ingles']
				razonamiento_cuantitativo = form.cleaned_data['razonamiento_cuantitativo']
				competencias_ciudadanas = form.cleaned_data['competencias_ciudadanas']
				puntaje_min = form.cleaned_data['puntaje_min']
				cupos = form.cleaned_data['cupos']
				info = form.cleaned_data['info']
				
				p = programasAcademico() #creo una instancia de la clase programaAcademico
				p.codigo = codigo
				p.nombre = nombre
				p.lectura_critica = lectura_critica
				p.matematicas = matematicas
				p.sociales = sociales
				p.naturales = naturales
				p.ingles = ingles
				p.razonamiento_cuantitativo = razonamiento_cuantitativo
				p.competencias_ciudadanas = competencias_ciudadanas
				p.puntaje_min = puntaje_min
				p.cupos = cupos
				p.info = info
				p.save() #guardar programa
				llamarMensaje= "Registro"
				mensaje= "Registro Satisfactorio!!!!!!"
				form = CarreraForm()
			
			else:
				llamarMensaje= "NoRegistro"
				mensaje = "DATOS INCORRECTOS!!!!!!"

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
				lectura_critica = form.cleaned_data['lectura_critica']
				matematicas = form.cleaned_data['matematicas']
				sociales = form.cleaned_data['sociales']
				naturales = form.cleaned_data['naturales']
				ingles = form.cleaned_data['ingles']
				razonamiento_cuantitativo = form.cleaned_data['razonamiento_cuantitativo']
				competencias_ciudadanas = form.cleaned_data['competencias_ciudadanas']
				puntaje_min = form.cleaned_data['puntaje_min']
				cupos = form.cleaned_data['cupos']
				info = form.cleaned_data['info']
				
				p = programasAcademico() #creo una instancia de la clase carrera
				p.codigo = codigo
				p.nombre = nombre
				p.lectura_critica = lectura_critica
				p.matematicas = matematicas
				p.sociales = sociales
				p.naturales = naturales
				p.ingles = ingles
				p.razonamiento_cuantitativo = razonamiento_cuantitativo
				p.competencias_ciudadanas = competencias_ciudadanas
				p.puntaje_min = puntaje_min
				p.cupos = cupos
				p.info = info
				p.save() #guardar y actualizo carrera
				llamarMensaje= "Registro"
				mensaje= "Actualización Satisfactoria!!!!!!"
			else:
				mensaje = "Datos erróneos"

		if request.method == "GET":
			form = EditarCarreraForm(initial={
				'codigo': p.codigo,
				'nombre': p.nombre,
				'lectura_critica': p.lectura_critica,
				'matematicas': p.matematicas,
				'sociales': p.sociales,
				'naturales': p.naturales,
				'ingles': p.ingles,
				'razonamiento_cuantitativo': p.razonamiento_cuantitativo,
				'competencias_ciudadanas': p.competencias_ciudadanas,
				'puntaje_min': p.puntaje_min,
				'cupos': p.cupos,
				'info': p.info,
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
		lista_carr = programasAcademico.objects.filter(status=True).order_by('codigo')
		paginator = Paginator(lista_carr,10)
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
		
def editar_password_view(request,username=None):
	mensaje = ""
	llamarMensaje = ""
	info=""
	form = EditarPasswordForm()
	if request.user.is_authenticated():
		if request.method == "POST":
			form = EditarPasswordForm(request.POST)
			if form.is_valid():
				password_actual = form.cleaned_data['password_actual']
				password_one = form.cleaned_data['password_one']
				password_two = form.cleaned_data['password_two']
				u = User.objects.get(username=username)
				if check_password(password_actual, u.password):
					u.set_password(password_one)
					#u.save()
					llamarMensaje= "Registro"
					mensaje= "Su contraseña se cambió correctamente!!!!!!"
					form = EditarPasswordForm()
				else:
					llamarMensaje="NoRegistro"
					mensaje="Contrasena Actual NO coincide"
			else:
				llamarMensaje="NoRegistro"
				mensaje="DATOS INCORRECTOS!!!!!!"
			
		ctx = {'form':form, 'mensaje':mensaje, 'llamarMensaje':llamarMensaje,'info':info}
		return render(request,'editar_password.html',ctx)
	else:
		return HttpResponseRedirect('/login')
		
def reporte_admitidos_view(request,pagina,carrera=None):
	iterator = itertools.count(1)#me genera un contador para el indice de la tabla
	if request.user.is_authenticated():
	#Metodo  para listar inscripciones
		#consulta por carrera, de mayor a menor puntaje y un cupo para 3
		list_admitidos = lista_admitidos.objects.all().order_by('carrera')
		paginator = Paginator(list_admitidos,20)
		try:
			page = int(pagina)
		except:
			page = 1
		try:
			admitidos = paginator.page(page)
		except:
			admitidos = paginator.page(paginator.num_pages)
			
		ctx = {'admitidos':admitidos,'iterator':iterator,'carrera':carrera}
		return render(request, 'reporte_admitidos.html',ctx)
	else:
		return HttpResponseRedirect('/login')	
		
def reportes_view(request):
	mensaje =""
	totalInscripciones= inscripciones.objects.count()
	totalInscripciones_tec_sitemas= inscripciones.objects.filter(carrera="TECNOLOGÍA EN SISTEMAS DE INFORMACIÓN").count()
	totalInscripciones_sitemas= inscripciones.objects.filter(carrera="INGENIERÍA DE SISTEMAS").count()
	totalInscripciones_quimica= inscripciones.objects.filter(carrera="INGENIERÍA QUÍMICA").count()
	totalInscripciones_tec_quimica= inscripciones.objects.filter(carrera="TECNOLOGÍA QUÍMICA").count()
	totalInscripciones_electronica= inscripciones.objects.filter(carrera="INGENIERÍA ELECTRÓNICA").count()
	totalInscripciones_tec_electronica= inscripciones.objects.filter(carrera="TECNOLOGÍA ELECTRÓNICA").count()
	
	if request.user.is_authenticated():
		ctx = {'msg':mensaje,'totalInscripciones':totalInscripciones,'totalInscripciones_tec_electronica':totalInscripciones_tec_electronica,
		'totalInscripciones_electronica':totalInscripciones_electronica,'totalInscripciones_quimica':totalInscripciones_quimica,
		'totalInscripciones_tec_sitemas':totalInscripciones_tec_sitemas,'totalInscripciones_sitemas':totalInscripciones_sitemas,
		'totalInscripciones_tec_quimica':totalInscripciones_tec_quimica}
		return render(request,'reportes.html',ctx)
	else:
		return HttpResponseRedirect('/login')	