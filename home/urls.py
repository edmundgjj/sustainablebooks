from django.contrib import admin
from django.urls import path, include
import home.views

urlpatterns = [
    path('', home.views.index),
    path('tradein', home.views.about_us, name="about_us")
]
