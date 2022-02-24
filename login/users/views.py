from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

def home(request):
    return render(request, "users/home.html")

def login(request):
    return render(request, "users/login.html")

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.info(request, f"Bonjour {username} votre compte est bien creer avec succes")
            return redirect('home')
    else:
        form=UserRegisterForm()
       
    
    context={
        'form': form
    }
    return render(request, "users/register.html", context)

def profile(request):
    return render(request, 'users/profile.html')