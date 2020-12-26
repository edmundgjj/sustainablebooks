from django.contrib import admin
from django.urls import path, include
import home.views

urlpatterns = [
    path('', home.views.index),
    path('story', home.views.about_us)
]