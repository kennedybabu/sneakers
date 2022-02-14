from unicodedata import name
from django.urls import path
from . import views


urlpatterns=[
    path('register/', views.registerUser,name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path("", views.landingpage, name='landingpage'),
    path("home/", views.home, name='home'),
    path('profile/<int:id>/', views.userProfile, name='user-profile'),
    path('update-user/', views.updateUser, name='update-user'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail')
]