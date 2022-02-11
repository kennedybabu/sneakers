from django.shortcuts import redirect, render
from .models import Shoe,User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
# Create your views here.



def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'something went wrong during registration')

    context = {
        'form':form
    }
    return render(request, 'app/register.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'username or password does not exist')
    return render(request, 'app/login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')


def landingpage(request):
    return render(request, 'app/landingpage.html')


def home(request):
    shoes = Shoe.objects.all()

    context = {
        'shoes':shoes
    }
    return render(request, 'app/home.html', context )