from django.db import models

# Create your models here.
class Main(models.Model):
    img=models.CharField(max_length=255)
    name=models.CharField(max_length=64,default='')
    tracked=models.IntegerField(default=1)
    # 修改默认的表明,class Meta修改元数据
    # 这里两个不一样，meta会建立3张表格，main作为主表，其他作为从表
    class meta:
        abstract=True

class Mainwhell(Main):
    class Meta:
        db_table='axf_wheel'

class MainNav(Main):
    class Meta:
        db_table="axf_nav"

class MainMustBuy(Main):
    class Meta:
        db_table="axf_mustbuy"

class MainShop(Main):
    class Meta:
        db_table='axf_shop'

class MainShow(Main):
    # 分类的id
    categoryid = models.IntegerField(default=1)
    # 名称
    brandname = models.CharField(max_length=64)
    # 图片
    img1 = models.CharField(max_length=255)
    # 分类
    childcid1 = models.IntegerField(default=1)
    # 商品编码
    productid1 = models.IntegerField(default=1)
    # 长名字
    longname1 = models.CharField(max_length=128)
    # 价格
    price1 = models.FloatField(default=1)
    # 超市价格
    marketprice1 = models.FloatField(default=0)

    img2 = models.CharField(max_length=255)
    childcid2 = models.IntegerField(default=1)
    productid2 = models.IntegerField(default=1)
    longname2 = models.CharField(max_length=128)
    price2 = models.FloatField(default=1)
    marketprice2 = models.FloatField(default=0)

    img3 = models.CharField(max_length=255)
    childcid3 = models.IntegerField(default=1)
    productid3 = models.IntegerField(default=1)
    longname3 = models.CharField(max_length=128)
    price3 = models.FloatField(default=1)
    marketprice3 = models.FloatField(default=0)

    class Meta:
        db_table = 'axf_mainshow'

class FoodType(models.Model):
    typeid=models.IntegerField(default=1)
    typename=models.CharField(max_length=255)
    childtypename=models.CharField(max_length=255)
    typesort=models.IntegerField(default=1)
    class Meta:
        db_table="axf_foodtype"

class Goods(models.Model):
    productid = models.IntegerField(default=1)
    productimg = models.CharField(max_length=255)
    productname = models.CharField(max_length=128)
    productlongname = models.CharField(max_length=255)
    isxf = models.BooleanField(default=False)
    esc =models.BooleanField(default=False)
    isc=models.CharField(max_length=64)
    price =models.FloatField(default=0)
    marketprice =models.FloatField(default=1)
    categoryid = models.IntegerField(default=1)
    childcid =models.IntegerField(default=1)
    childcidname =models.CharField(max_length=128)
    dealerid = models.IntegerField(default=1)
    storenums =models.IntegerField(default=1)
    productnum =models.IntegerField(default=1)

    class meta:
        db_table = 'axf_goods'