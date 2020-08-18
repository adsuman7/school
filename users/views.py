from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.

class Register(View):

	def post(self,request,*args,**kwargs):
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'your account has been created you have been login {username}!')
			return redirect('login')
	def get(self, request, *args, **kwargs):
		form=UserRegisterForm()
		return render(request,'users/register.html',{'form':form})

class Update(LoginRequiredMixin,View):
	def post(self,request,*args,**kwargs):
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'your account has been updated')
			return redirect('/')
	def get(self,request,*args,**kwargs):
		u_form=UserUpdateForm(instance=request.user)
		p_form =ProfileUpdateForm(instance=request.user.profile)
		context= {
		'u_form':u_form,
		'p_form':p_form
		}

		return render(request,'users/profile.html',context)

class Profile_View(LoginRequiredMixin,View):
	def get(self,request,*args,**kwargs):
		return render(request,'users/teacher_info.html')
