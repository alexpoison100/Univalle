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
	status		=models.BooleanField(default=True)


	def __unicode__(self):
		return self.nombre

class inscripciones(models.Model):
	cedula		=models.BigIntegerField(null=False, unique=True, primary_key=True)
	nombre		=models.CharField(max_length=100)
	apellido	=models.CharField(max_length=100)
	snp			=models.CharField(max_length=50)
	ref_pago	=models.IntegerField()
	carrera		=models.CharField(max_length=100)
	status		=models.BooleanField(default=True)

	def __str__(self):
		return '%s - %s' % (self.cedula, self.snp)
	 
