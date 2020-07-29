from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
# from app01.models import MainWheel

# Create your views here.
def test(request):
    # obj=User.objects.get(pk=1)
    # return HttpResponse(obj.username)
    return render(request,'base.html')

def home(request):
    # objs=MainWheel.objects.all()
    # data={
    #     'title':"首页",
    #     'main_wheels':objs
    # }


    # return render(request,'main/home.html',data)
    return render(request,'main/home.html')

def market(request):
    return render(request,'main/market.html')

def cart(request):
    return render(request,'main/cart.html')

def mine(request):
    return render(request,'main.mine.html')