from django.contrib import admin
from app03.models import *
# Register your models here.


# class QuestionAdmin(admin.ModelAdmin):
#     fields=['pub_date','question']


class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        ("这是标题栏",{'fields':["question"]}),
        ("这是第二个",{'fields':['pub_date']})
    ]

    inlines=[ChoiceInline]

    list_display=('question','pub_date','was_published_recently')

    list_filter=['pub_date']
    search_fields=['question']
    
# 1.添加到页面
# 2.变换字段顺序
# 3.字段分类加标题
# 4.1对多添加多
# 5.列表显示显示多个字段
# 5.2函数显示值
# 6.过滤选项表
# 7.查询
# 8.定制admin网页
admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)