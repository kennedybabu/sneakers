from django.shortcuts import render
from .models import Shoe
# Create your views here.


def landingpage(request):
    return render(request, 'app/landingpage.html')

def home(request):
    shoes = Shoe.objects.all()


    context = {
        'shoes':shoes
    }
    return render(request, 'app/home.html', context )