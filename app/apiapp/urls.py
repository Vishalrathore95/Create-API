

from django.urls import path
from . import views  # Importing views module from the current directory

urlpatterns = [
    path('', views.index, name="index"),  
]
