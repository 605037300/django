from django.urls import path,re_path
from app01 import views

urlpatterns = [
    path('test/',views.test,name='test'),
    path('home/',views.home,name='home'),
    path('market/',views.market,name='market'),
    re_path(r'^marketwithp/(?P<typeid>\d+)/$',views.marketwithp,name="marketwithp"),

    path('cart/',views.cart,name='cart'),
    path('mine/',views.mine,name='mine'),

   
]