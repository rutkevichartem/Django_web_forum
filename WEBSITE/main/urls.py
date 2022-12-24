from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('contact-us', views.contact, name='contact'),
    path('create-task', views.create, name='create'),
]