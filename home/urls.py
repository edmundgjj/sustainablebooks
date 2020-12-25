from django.contrib import admin
from django.urls import path, include
import home.views

urlpatterns = [
    path('', home.views.index, name='homepage'),
    path('story', home.views.about_us, name='about_us')
]