from django.db import models

# Create your models here.
class Main(models.Model):
    img=models.CharField(max_length=255)
    name=models.CharField(max_length=64,default='')
    tracked=models.IntegerField(default=1)
    # 修改默认的表明,class Meta修改元数据
    class Meta:
        abstract=True

class Mainwhell(Main):
    class Meta:
        db_table='axf_wheel'

class MainNav(Main):
    class Meta:
        db_table="axf_nav"