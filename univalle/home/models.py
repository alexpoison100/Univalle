# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def url(obj, filename):
		ruta ="MultimediaData/Users/%s/%s"%(obj.user.username,filename)
		return ruta
		
class userProfile(models.Model):

	user 		= models.OneToOneField(User)
	photo		= models.ImageField(upload_to=url)
	e_mail		= models.EmailField(max_length=254)

	def __unicode__(self):
		return self.user.username
	
class programasAcademico(models.Model):
	codigo		=models.BigIntegerField(null=False, unique=True, primary_key=True)
	nombre		=models.CharField(max_length=100)
	lectura_critica				=models.FloatField()
	matematicas					=models.FloatField()
	sociales					=models.FloatField()
	naturales					=models.FloatField()
	ingles						=models.FloatField()
	razonamiento_cuantitativo	=models.FloatField()
	competencias_ciudadanas		=models.FloatField()
	puntaje_min	=models.IntegerField()
	info		=models.CharField(max_length=300)
	status		=models.BooleanField(default=True)


	def __unicode__(self):
		return self.nombre

class inscripciones(models.Model):
	cedula		=models.BigIntegerField(null=False, unique=True, primary_key=True)
	nombre		=models.CharField(max_length=100)
	apellido	=models.CharField(max_length=100)
	snp			=models.CharField(max_length=50)
	lectura_critica				=models.IntegerField()
	matematicas					=models.IntegerField()
	sociales					=models.IntegerField()
	naturales					=models.IntegerField()
	ingles						=models.IntegerField()
	razonamiento_cuantitativo	=models.IntegerField()
	competencias_ciudadanas		=models.IntegerField()
	colegio		=models.CharField(max_length=100)
	ref_pago	=models.IntegerField()
	carrera		=models.CharField(max_length=100)
	status		=models.BooleanField(default=True)

	def __str__(self):
		return '%s - %s' % (self.cedula, self.snp)

class lista_admitidos(models.Model):
	cedula		=models.BigIntegerField(null=False, unique=True, primary_key=True)
	nombre		=models.CharField(max_length=100)
	apellido	=models.CharField(max_length=100)
	puntaje		=models.FloatField()
	carrera		=models.CharField(max_length=100)
	status		=models.BooleanField(default=True)
	
	def __str__(self):
		return str(self.cedula)
	
	
	
	
	
	