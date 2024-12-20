from django.db import models

# Create your models here.
class Product(models.Model):
	Pid = models.IntegerField()
	Pname = models.CharField(max_length=20)
	Price = models.FloatField()
	
	def __str__(self):
		return self.Pname