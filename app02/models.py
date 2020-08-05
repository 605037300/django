from django.db import models

# Create your models here.

class Books(models.Model):
    bookname=models.CharField(max_length=255)
    booktype=models.OneToOneField('BookType',on_delete=models.CASCADE,default=1)
    bookprice=models.DecimalField(decimal_places=2,max_digits=6)
    author=models.ManyToManyField('Author')
    pub_date=models.DateField()
    publish=models.ForeignKey('Publish',on_delete=models.CASCADE)

class BookType(models.Model):
    typename=models.CharField(max_length=20)

class Author(models.Model):
    authorname=models.CharField(max_length=64)
    authorinfo=models.OneToOneField("Info",on_delete=models.CASCADE)

class Info(models.Model):
    gender_choice=((0,"保密"),(1,"男"),(2,'女'))
    gender=models.SmallIntegerField(gender_choice)
    addr=models.CharField(max_length=255)
    age=models.IntegerField(default=1)

class Publish(models.Model):   
    publishname=models.CharField(max_length=255)
    city=models.OneToOneField('City',on_delete=models.CASCADE)
    tel=models.CharField(max_length=15)
    email=models.EmailField()

class City(models.Model):
    cityname=models.CharField(max_length=100)
