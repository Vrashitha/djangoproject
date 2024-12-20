from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def view1(request):
	S="<h1> welcome to django Session"
	
	return HttpResponse(S)

