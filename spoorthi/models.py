from django.db import models

# Create your models here.
class Register(models.Model):
	event = models.CharField(max_length=100,default="")
	full_name = models.CharField(max_length=100,default="")
	email = models.EmailField(max_length=254)
	number = models.CharField(max_length=100,default="")
	college = models.CharField(max_length=100,default="")
	description = models.TextField(max_length=1000,default="")
	
	def __str__(self):
		return self.email