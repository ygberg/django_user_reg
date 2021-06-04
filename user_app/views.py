from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from user_app.models import UserProfile
from user_app.forms import RegForm,UserForm
# Create your views here.
from django.core.files.storage import default_storage


def register_user(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        form2 = RegForm(request.POST, request.FILES)
        if  form.is_valid() and form2.is_valid():
            # user = UserProfile.objects.get(user_name='user_name',email='email',password='password')
            # reg =UserProfile.objects.get(user='user',portfoliosite='portfoliosite'
            #                                                             ,profile_pic='profile_pic')
            # img = form2.clean_data.get("Profile_pic")
            # profile_picture = default_storage.save(img.name, img)
            userinfo =UserProfile.objects.get_or_create(username=request.username,email=request.email,password=request.password)
            portinfo = UserProfile.object.get_or_create(username=request.username,portfoliosite=request.portfoliosite,profile_pic=request.profile_pic)
            userinfo.save()
            portinfo.save()
            return HttpResponse( 'Thank you for signing up with us')
    else:
            
       
        form = UserForm()
        form2 = RegForm()
           
    return render(request,'register_user.html',{'form':form,'form2':form2})