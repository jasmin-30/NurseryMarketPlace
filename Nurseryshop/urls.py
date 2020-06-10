from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Nurseryshop import views

urlpatterns = [
    path('', views.HomepageView, name='home'),
    path('login/', views.LoginView, name='login'),
    path('register/', views.RegisterView, name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
