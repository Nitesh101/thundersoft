from django.shortcuts import render
from dappx.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	return render(request,'dappx/index.html')
@login_required
def special(request):
	return HttpResponse('You are logged in !')

@login_requred
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


def register(request):
	register = False
	if request.method = 'POST':
		user_form  = UserForm(data=request.POST)
		profile_form = UserForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=Flase)
			profile.user = user
			if 'profile_pic' in request.FIELS:
				print('found it')
				profile.profile_pic = request.FIELS['profile_pic
]
			profile.save()
			registered = True
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()
	return render(request,'dappx/registration.html',{'user_form':user_form,'registered':registered})

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
				return HttpResponse("Your account was inactive")
		else:
			print ("someone trid to login and failed")
			print ("They used username: {} and password : {} ".format(username,password))
	else:
		return render(request,'dappx/login.html',{})

		
