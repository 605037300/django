from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Question2(models.Model):
    models.AutoField(primary_key=True)

    q_text=models.CharField(max_length=100)
    pub_date=models.DateTimeField("xx")
    def was_recently_published(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)

    def __str__(self):
        return self.q_text

class Choice2(models.Model):
    c_text=models.CharField(max_length=100)
    c_num=models.IntegerField(default=0)
    question=models.ForeignKey('Question2',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.c_text