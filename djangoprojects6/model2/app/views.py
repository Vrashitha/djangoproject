from django.shortcuts import render
from app.models import Student
# Create your views here.
def view(request):
	S = Student.objects.all()
	d={'Stud':S}
	return render(request,'html page/1.html',d)
