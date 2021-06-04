from django.db.models import fields
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from user_app.models import UserProfile
from user_app.forms import RegForm,UserForm
# Create your views here.
from django.core.files.storage import default_storage


def index(request):
    return render(request,'index.html')

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


        else : 
            print(user_form.errors, profile_form.errors)
    
    else:

        user_form = UserForm()
        profile_form = RegForm()

    return render(request,'register_user.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})