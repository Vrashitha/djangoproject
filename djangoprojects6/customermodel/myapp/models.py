from django.db import models

# Create your models here.
class Customer(models.Model):
	Cid = models.IntegerField()
	Fname = models.CharField(max_length=20)
	Lname = models.CharField(max_length=30)
	Lid = models.IntegerField()
	def __str__(self):
		return self.Fname