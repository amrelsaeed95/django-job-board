from django.shortcuts import redirect, render
from .forms import SignupForm
from django.contrib.auth import authenticate, login
# Create your views here.


def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']   #yegebhom
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)  #yt2kd enhm mwgden
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    
    return render(request,'registeration/signup.html',{'form':form}) 

