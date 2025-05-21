from django.shortcuts import render,redirect
from .models import *
from .forms import ProfileForm

from django.contrib import messages

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import re
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def register(request):
    if request.method=='POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if password==password1:
            if CustomUserModel.objects.filter(username=username).exists():
                messages.error(register,"Username already exists!!!")
                return redirect('register')
            
            if CustomUserModel.objects.filter(email=email).exists():
                messages.error(register,"Email already exists!!!")
                return redirect('register')
            
            if not re.search(r"[A-Z]",password):
                messages.error(request,'your password should contain at least one upper case')
                return redirect('register')
            if not re.search(r"\d",password):
                messages.error(request,'your password should contain at least one digit')
                return redirect('register')
            if not re.search(r"\W",password):
                messages.error(request,'your password should contain at least specific character')
                return redirect('register')
            
            try:
                validate_password(password) #abc
                CustomUserModel.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password,phone=phone,street_address=address)
                return redirect('log_in')
            
            except ValidationError as e:
                for i in e.messages:
                    messages.error(request,i)
                return redirect('register')

        else:
            messages.error(request,"Your password and confirm password doesn't match!!!")
            return redirect('register')

    return render(request,'accounts/register.html')



def log_in(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me') #on or off

        if not CustomUserModel.objects.filter(username=username).exists():
            messages.error(request,'username is not register yet')
            return redirect('log_in')
        
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            if remember_me:
                request.session.set_expiry(12345678)
            else:
                request.session.set_expiry(0)
            next = request.POST.get('next','') #/about/

            return redirect(next if next else'index') #shorthand if-else
        else:
            messages.error(request,'password does not match!!!!')
            return redirect('log_in')
        

        
    next=request.GET.get('next','')
    return render(request,'accounts/login.html',{'next':next})


@login_required(login_url='log_in')
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    return render(request,'accounts/change_password.html',{'form':form})


@login_required(login_url='log_in')
def profile(request):
    return render(request,'profile/profile.html')

def update_profile(request):
    profile,created=Profile.objects.get_or_create(user=request.user)
    form=ProfileForm(instance=profile)
    context={
        'form':form
    }
    return render(request,'profile/update_profile.html',context)