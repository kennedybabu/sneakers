from django.shortcuts import get_object_or_404, redirect, render
from .models import Product,User, Category
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


def home(request, category_slug=None):
    Products = Product.objects.all()
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Products.filter(category=category)

    context = {
        'products':products,
        'categories':categories,
        'category': category
    }
    return render(request, 'app/home.html', context )


def product_detail(request,id, slug):
    product = get_object_or_404(Product, id = id, slug=slug)

    context = {
       'product':product 
    }
    return render(request, 'app/product_detail.html', context)
