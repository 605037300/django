from django.shortcuts import render,HttpResponse,Http404,get_object_or_404,redirect,reverse
from django.utils import timezone
# Create your views here.
from app03.models import *

from django.views import generic
def test(request):
    cyear=timezone.now().year
    q=Question.objects.get(pk=1)
    c=Choice.objects.filter(question__pub_date__year=cyear)
    print(c)
    print(q.choice_set.all())


# def index(request):
#     latestq=Question.objects.order_by("-pub_date")[:5]
#     data={
#         "latestq":latestq
#     }
#     return render(request,'app03/index.html',data)

class IndexView(generic.ListView):
    template_name='app03/index.html'
    context_object_name='latestq'
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]



# def detail(request,question_id):
#     try:
#         question=Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         return redirect(reverse("app03:index"))
#     # question=get_object_or_404(Question,pk=question_id)
#     return render(request,"app03/detail.html",{"question":question})

class DetailView(generic.DetailView):
    model=Question
    template_name='app03/detail.html'



def result(request,question_id):
    return HttpResponse("bbb")

def vote(request,question_id):
    print(request.POST)
    question=get_object_or_404(Question,pk=question_id)
    data={
        "question":question,
        "error_message":"错误"
    }
    try:
       selected_choice=question.choice_set.get(pk=request.POST.get("choice"))
    except (KeyError,Choice.DoesNotExist):
        return render(request,"app03/detail.html",)

    selected_choice.vote+=1
    selected_choice.save()
    return redirect(reverse('app03:result',args=(question.id,)))

def result(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"app03/result.html",{"question":question})
   
    