from django.shortcuts import render
from django.http import HttpResponse
def sub1(request):
	n1=int(input("enter a num1:"))
	n2=int(input("enter a num2:"))
	n3=n1-n2
	return HttpResponse(str(n3))


def mul1(request):

	n1=int(input("enter a num1:"))
	n2=int(input("enter a num2:"))
	n3=n1*n2
	return HttpResponse(str(n3))



# Create your views here.
