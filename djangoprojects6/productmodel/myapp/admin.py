from django.contrib import admin
from myapp.models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	i=['Pid','Pname','Price']
admin.site.register(Product,ProductAdmin)