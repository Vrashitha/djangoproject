from django.contrib import admin
from app.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	i=['Class','Name','Phno','Usn','Add','Marks']
admin.site.register(Student,StudentAdmin)
