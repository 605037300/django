from django.shortcuts import render,HttpResponse,get_object_or_404,redirect,reverse

# Create your views here.
from app04.models import *
from django.views import generic


class IndexView(generic.ListView):
    template_name='app04/index.html'
    context_object_name='latest_q'
    def get_queryset(self):
        return Question2.objects.order_by("-pub_date")[:5]

def vote(request,question_id):
    print(request.POST)
    try:
        q=get_object_or_404(Question2,pk=question_id)
        selected_choice=q.choice2_set.get(pk=request.POST.get('choice'))
    except(KeyError,Choice2.DoesNotExist):
        return render(request,'app04/detail.html',{"err_message":'有异常'})
    
    selected_choice.c_num+=1
    selected_choice.save()
    return redirect(reverse('app04:result',args=(q.pk,)))



class DetailView(generic.DetailView):
    model=Question2
    template_name='app04/detail.html'

class ResultView(generic.DetailView):
    models=Question2
    template_name='app04/result.html'
    

# def result(request,question_id):
#     q=get_object_or_404(Question2,pk=question_id)
#     return render(request,'app04/result.html',{"q":q})