from django.shortcuts import render
from myapp.models import Customer

# Create your views here.
def myview(request):
	C = Customer.objects.all()
	d={'Cust':C}
	return render(request,'htmlpage/1.html',d)
