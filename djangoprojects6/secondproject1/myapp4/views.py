from django.shortcuts import render
from django.http import HttpResponse
def view1(request):
	a = "good morning"
	return HttpResponse(a)
	


# Create your views here.
