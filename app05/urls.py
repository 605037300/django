from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index,name="index"),
    path('login/',views.login),
    path('logout/',views.logout),
    path('register/',views.register),
    path('confirm/',views.confirm),
    path('tt/',views.tt)
]