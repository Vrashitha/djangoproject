from django.contrib import admin
from myapp.models import Employee


# Register your models here.


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):  
	i=['Eid','Ename','Ephno','Sal','Add','Designation']
admin.site.register(Employee,EmployeeAdmin)