from django.shortcuts import render

# Create your views here.
def myView(request):
	return render(request,'htmlpage/1.html')
