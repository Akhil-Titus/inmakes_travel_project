from . import views
from django.urls import path, include

app_name = 'travel_app'

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('result/', views.addition, name='addition'),
]
