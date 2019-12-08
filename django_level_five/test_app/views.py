from django.shortcuts import render
from test_app.forms import userForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.

def index(request):
	return render(request,'test_app/index.html',{})
	
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))
	
def register(request):
	registered = False
	
	if request.method == 'POST':
		user_form = userForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			
			registered = True
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form = userForm()
		profile_form = UserProfileInfoForm()
	return render(request,'test_app/register.html',{'user_form':user_form, 'profile_form':profile_form, 'registered':registered})
	
	
def user_login(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Account not Active!")
		else:
			print("Someone tried with invalid details!")
			print("Username: {} \n Password: {}".format(username,password))
			return HttpResponse("Invalid account details!")
	else:
		return render(request,'test_app/login.html',{})