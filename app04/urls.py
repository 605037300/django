from django.urls import path,include
from app04.views import *

urlpatterns = [
    path('',IndexView.as_view(),name="index"),
    path('<int:pk>/',DetailView.as_view(),name='detail'),
    path('<int:question_id>/vote/',vote,name="vote"),
    path('<int:pk>/result/',ResultView.as_view(),name='result'),
    # path('<int:question_id>/result/',result,name='result'),

]
