from django.shortcuts import redirect, render
from .forms import SignupForm , UserForm , ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse 

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






def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})



def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method=='POST': # el data el hatet-save
        userform = userform = UserForm(request.POST,instance=request.user)   
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)  # d5lt el data el lsa rag3a w el data el mwgooda alsn el b3d el else
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False) # false 3shan lsa h7dd el user
            myprofile.user = request.user # el sh5s el 3aml login 7alyn
            myprofile.save()
            return redirect(reverse('accounts:profile'))
             
    else : # el data el zahra
        userform = UserForm(instance=request.user)   #the current user
        profileform = ProfileForm(instance=profile)  
    
    
    return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})
