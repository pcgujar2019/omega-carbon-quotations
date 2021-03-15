"""omega_carbon_quotations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quotations import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth URL's
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Main app HOME URL
    path('', views.home, name='home'),
    
    # Create quotation URL
    path('create-step1/', views.createquotationstep1, name='createquotationstep1'),
    path('create-step2/', views.createquotationstep2, name='createquotationstep2'),
    path('create-step3/', views.createquotationstep3, name='createquotationstep3'),
    
    # Search quotation URL
    path('search/', views.searchquotation, name='searchquotation'),
    
    # Show all clients URL
    path('clients/', views.clientslist, name='clientslist'),
    
]
