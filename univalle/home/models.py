from django.db import models
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
def url(obj, filename):
		ruta ="MultimediaData/Users/%s/%s"%(obj.user.username,filename)
		return ruta
		
class userProfile(models.Model):
	
	user 		= models.OneToOneField(User)
	photo		= models.ImageField(upload_to=url)
	telefono	= models.CharField(max_length=30)
	e_mail		= models.EmailField(max_length=254)

	def __unicode__(self):
		return self.user.username
	
class programasAcademico(models.Model):
	codigo		=models.IntegerField()
	nombre		=models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class inscripciones(models.Model):
	cedula		=models.IntegerField()
	nombre		=models.CharField(max_length=100)
	apellido	=models.CharField(max_length=100)
	snp			=models.CharField(max_length=50)
	carrera		=models.CharField(max_length=100)

	def __str__(self):
	 return '%s - %s  %s - %s' % (self.cedula, self.nombre, self.apellido, self.snp)
		
		
		
		
		