from django.shortcuts import render
from myapp.models import Product
# Create your views here.
def myview(request):
	P = Product.objects.all()
	d={'Prod':P}
	return render(request,'htmlpage/1.html',d)
