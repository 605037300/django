from django.urls import path
from app01 import views

urlpatterns = [
    path('test/',views.test,name='test'),
    path('home/',views.home,name='home'),
    path('market/',views.market,name='market'),
    path('cart/',views.cart,name='cart'),
    path('mine',views.mine,name='mine'),
]