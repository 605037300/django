from django.shortcuts import render,HttpResponse
from app02.seeds import *
from app02.models import *
import random,string,datetime

# Create your views here.
def seed(request):
    if not City.objects.all():
        for x in CITYS:
            city=City.objects.create(cityname=x)
            city.save()

    if not Publish.objects.all():
        for i,v in enumerate(PUBLISHS):
            cityobj=City.objects.filter(id=i+1).first()
            Publish.objects.create(publishname=v,city=cityobj,tel=''.join(random.sample(string.digits,8)),email="1".join(random.sample(string.ascii_letters,3))+"@qq.com")

    if not Info.objects.all():
        for i in range(20):
            Info.objects.create(gender=random.choice(range(3)),addr="".join(random.sample(string.ascii_letters,12)))

    if not Author.objects.all():
        for i in range(20):
            infoobj=Info.objects.get(id=i+1)
            Author.objects.create(authorname="".join(random.sample(string.ascii_letters,8)),authorinfo=infoobj)

    if not BookType.objects.all():
        for i,v in enumerate(BOOKTYPES):
            BookType.objects.create(typename=v)

    c=Author.objects.all().count()
    p=Publish.objects.all().count()
   
   

    if not Books.objects.all():
        for i in range(10):
            bookname="".join(random.sample(string.ascii_letters,8))
            booktype=BookType.objects.filter(id=i+1).first()
            bookprice=random.uniform(1,40)
            author_id=Author.objects.filter(id=random.choice(range(1,c))).first().pk
            pub_date=datetime.datetime.now()
            publish_id=Publish.objects.filter(id=random.choice(range(1,p))).first()

            print(author_id,publish_id)
            Books.objects.create(bookname=bookname,booktype=booktype,bookprice=bookprice,pub_date=pub_date,publish=publish_id)
    else:
        print(a)
        # t=random.sample(Author.objects.all(),4)
        # print(t)
        # for i in range(Books.objects.all().count()):
        #     b=Books.objects.filter(pk=i).first()
        #     authorlist=[]
        #     t=random.sample(Author.objects.all(),4)
          
        #     b.add(Author.objects.filter)
    
    


    return HttpResponse('c')


