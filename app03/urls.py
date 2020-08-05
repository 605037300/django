from django.urls import path,include
from app03 import views

urlpatterns = [
    path("",views.IndexView.as_view(),name='index'),
    path("<int:pk>/",views.DetailView.as_view(),name='detail'),
    path("<int:question_id>/results/",views.result,name='result'),
    path('<int:question_id>/vote/',views.vote, name='vote'),
]