"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.Home, name="home"),
    path('About', view.about, name="about"),
    path('contact',view.contact,name="contact"),
    path('Login',view.login,name="login"),
    path('Registration',view.registration,name='res'),
    path('Feedback',view.feedback,name="feedback"),
    path('gallery',view.gallery,name="gallery"),
    path('Info',view.info,name="info"),
    path('Form',view.form,name="form"),
    path('logout',view.logout,name="logout"),
]
