from django.contrib import admin
from .models import *
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model=Choice2
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        ("这是回顾联系",{'fields':['q_text']}),
        ("xx",{'fields':['pub_date']})
    ]

    inlines=[ChoiceInline]



admin.site.register(Question2,QuestionAdmin)
