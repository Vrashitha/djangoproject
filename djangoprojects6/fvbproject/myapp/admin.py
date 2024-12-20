from django.contrib import admin
from myapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	i=['sno','sname','smarks','saddr']
admin.site.register(Student,StudentAdmin)