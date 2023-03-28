from django.shortcuts import render,redirect
from .forms import SignUpForm,EditUserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        fm=SignUpForm(request.POST)
        # print(fm)
        if fm.is_valid():
            messages.success(request,'Account created successfully!!!')
            fm.save()
    else:
        fm=SignUpForm()
    return render(request,'App/signup.html',{'forms':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            print(request.POST)
            if fm.is_valid():
                print("1")
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                print(user)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile')
        else:
            fm=AuthenticationForm()
        return render(request,'App/login.html',{'forms':fm})
    
    else:
        return HttpResponseRedirect('/profile')

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm=EditUserForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,'Profile change successfully!!!')
                fm.save()
        else:
            fm=EditUserForm(instance=request.user)
        return render(request,'App/user_profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login')


def user_pass_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'password updated successfully!!!')
                update_session_auth_hash(request,user=request.user)
                return redirect('/profile')
        else:
            fm=PasswordChangeForm(user=request.user)    
        return render(request,'App/changepassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login')
    

def user_logout(request):
    logout(request)
    return redirect('/login/')


