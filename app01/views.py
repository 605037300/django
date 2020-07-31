from django.shortcuts import render,HttpResponse,redirect,reverse
from django.contrib.auth.models import User
from app01.models import Mainwhell,MainNav,MainMustBuy,MainShop,MainShow,Goods,FoodType
from app01.views_constant import *
# Create your views here.
def test(request):
    # obj=User.objects.get(pk=1)
    # return HttpResponse(obj.username)
    return render(request,'base.html')

def home(request):
    whellobjs=Mainwhell.objects.all()
    navobjs=MainNav.objects.all()
    mustobjs=MainMustBuy.objects.all()
    shops=MainShop.objects.all()
    shop0_1=shops[0:1]
    shop1_3=shops[1:3]
    shop3_7=shops[3:7]
    shop7_11=shops[7:11]
    main_show=MainShow.objects.all()

    data={
        'title':"首页",
        'main_wheels':whellobjs,
        'main_navs':navobjs,
        'main_mustbuy':mustobjs,
        'shop0_1':shop0_1,
        'shop1_3':shop1_3,
        'shop3_7':shop3_7,
        'shop7_11':shop7_11,
        'main_shows':main_show
    }


    return render(request,'main/home.html',data)
    return render(request,'main/home.html')

def market(request):
    return HttpResponse(ALL_TY)
    # return redirect(reverse('app01:marketwithp',kwargs={"typeid":1001}))

def marketwithp(request,typeid):
    foodtps=FoodType.objects.all()
    goods=Goods.objects.filter(categoryid=typeid)
    data={
        "titile":"商城",
        'foodstyle':foodtps,
        'goods':goods,
        'typeid':typeid
    }
    return render(request,"main/market.html",data)
    # return HttpResponse(typeid)


def cart(request):
    return HttpResponse(ALL_TY)
def mine(request):
    return render(request,'main.mine.html')