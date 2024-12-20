from django.db import models

# Create your models here.
class Student(models.Model):
	Class = models.CharField(max_length=20)
	Name = models.CharField(max_length=20)
	Phno = models.IntegerField()
	Usn = models.CharField(max_length=25)
	Add = models.CharField(max_length=30)
	Marks = models.CharField(max_length=20)
	

	def __str__(self):
		return self.Name