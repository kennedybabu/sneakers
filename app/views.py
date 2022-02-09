from django.shortcuts import render

# Create your views here.


def landingpage(request):
    return render(request, 'app/landingpage.html')

def home(request):
    return render(request, 'app/home.html')