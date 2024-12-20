from django.shortcuts import render
from myapp.models import Employee
# Create your views here.
def myview(request):
	E=Employee.objects.all()
	d={'emp':E}
	return render(request,'htmlpage/1.html',d)