from django.shortcuts import get_object_or_404, redirect, render
from .models import Product,User, Category
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from cart.forms import CartAddProductForm
from .forms import UserForm, MyUserCreationForm

# Create your views here.



def registerUser(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
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


def home(request,category_slug=None):
    category = None
    products = Product.objects.all()
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)


    context = {
        'products':products,
        'categories':categories,
    }
    return render(request, 'app/home.html', context )



def userProfile(request, id):
    user = User.objects.get(id=id)
    
    context = {
        'user':user
    }
    return render(request, 'app/profile.html', context)


def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', id= user.id)

    context = {
        'form':form
    }
    return render(request, 'app/update-user.html', context)

def product_detail(request,id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()

    context = {
       'product':product,
       'cart_product_form':cart_product_form,
    }

    return render(request, 'app/product_detail.html', context)
