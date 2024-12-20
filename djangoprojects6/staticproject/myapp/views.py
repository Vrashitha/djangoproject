from django.shortcuts import render

# Create your views here.
def view1(request):
	myname="sumathi"
	favplayer="virat"
	favanimal="dog"
	favcolor="black"
	d={'name':myname,'player':favplayer,'animal':favanimal,'color':favcolor}
	return render(request,"htmlpage/1.html",d)
