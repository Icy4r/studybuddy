from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from userprofile.models import UserProfile
from useraccounts.forms import loginForm
from django.http import HttpResponseRedirect


# Create your views here.
def login_view(request):

    if request.method == "POST":
        form = loginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            # check if user exists
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                login_failed = "Username and password do not match any existing account."
                HttpResponseRedirect('/useraccounts/login/')

    else:
        form = loginForm()
        login_failed = ""


    context = {
        'form': form,
        'login_failed': login_failed
    }

    return render(request, 'useraccounts/login.html', context=context)

def create_account(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
    
        if form.is_valid():
            form.save()

            # create UserProfile
            u = User.objects.get(username=form.cleaned_data['username'])
            userProfile = UserProfile(user=u, name=u.username)
            userProfile.save()
            
            return HttpResponseRedirect('/useraccounts/login/') 

    else:
        form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'useraccounts/createaccount.html', context=context)
