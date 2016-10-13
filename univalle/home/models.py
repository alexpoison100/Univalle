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
	
