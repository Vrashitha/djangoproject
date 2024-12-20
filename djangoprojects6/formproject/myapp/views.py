from django.shortcuts import render
from myapp.forms import StudentForm


# Create your views here.
def FormView(request):
	f=StudentForm()
	if request.method=="POST":
		f=StudentForm(request.POST)
		if f.is_valid():
			name=f.cleaned_data['name']
			USN=f.cleaned_data['USN']
			mob=f.cleaned_data['mob']
			branch=f.cleaned_data['branch']
			Email=f.cleaned_data['Email']
			d={'name':name,'USN':USN,'mob':mob,'branch':branch,'Email':Email}
			return render(request,'htmlpage/output.html',d)
	d={'form':f}
	return render(request,'htmlpage/input.html',d)
