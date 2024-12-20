from django.db import models

# Create your models here.


# Create your models here.
class Employee(models.Model):
	Eid = models.IntegerField()
	Ename = models.CharField(max_length=20)
	Ephno = models.IntegerField()
	Sal = models.FloatField()
	Add = models.CharField(max_length=30)
	Designation = models.CharField(max_length=20)


	def  __str__(self):
		return(self.Ename)

