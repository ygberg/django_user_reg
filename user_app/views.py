from django.db.models import fields
from django.http import request
from django.http.response import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render
from user_app.models import UserProfile
from user_app.forms import RegForm,UserForm
from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
# Create your views here.


def index(request):
    return render(request,'index.html')

@login_required
def log_out(reuqest):
    logout(reuqest)
    return HttpResponseRedirect(reverse('index.html'))

@login_required
def special_site(request):
    return render(request,'special_site.html',{})

def register_user(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = RegForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                ppic = request.FILES['profile_pic']
                profile.profile_pic = ppic
                profile.save()
                registered = True

                
            profile.save()
            registered = True

        else : 
            print(user_form.errors, profile_form.errors)
    
    else:

        user_form = UserForm()
        profile_form = RegForm()

    return render(request,'register_user.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



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
                HttpResponse('user not active')

        else:
            print('some one tried to login but failed')
            print(f'usernam: {username} and with password: {password}')
            HttpResponse('wrong username or passowrd')

    else:
        return render(request,'user_login.html',{})