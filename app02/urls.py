from django.urls import path,include
from app02 import views

urlpatterns = [
    path("seed/",views.seed,name='seed'),
   
]