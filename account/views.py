from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,FormView,CreateView,View
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

class LandingView(TemplateView):
    template_name="index.html"


class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            print(uname,pswd)
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"Login SuccessFull!!")
                return redirect('uhome')
            else:
                messages.error(request,"Login Failed!! Invalid Username/Password!!")
                return redirect('sin')
        else:
            return render(request,"login.html",{"form":form_data})

class SignUpView(CreateView):
    template_name="reg.html"
    form_class=RegsiterForm
    success_url=reverse_lazy('sin')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        messages.success(self.request,"Registration Success!!")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"Registration Success!!")
        return super().form_invalid(form)
    

class SignOutView(View):
    def get(self,request):
        logout(request)
        messages.error(request,"Sign Out SuccessFull!!")
        return redirect('sin')