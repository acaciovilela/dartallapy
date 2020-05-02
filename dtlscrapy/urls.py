from django.urls import path, include
from . import views

app_name = 'scrapy'

urlpatterns = [
    path('', views.index, name="index"),
]
