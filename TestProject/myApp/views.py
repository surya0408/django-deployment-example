from django.shortcuts import render

# Create your views here.

def index(request):
	dict = {'cntxt_dict':'Surya' }
	return render(request,'myApp/index.html',context=dict)
	
def other(request):
	return render(request,'myApp/other.html')
	
def last(request):
	return render(request,'myApp/last.html')