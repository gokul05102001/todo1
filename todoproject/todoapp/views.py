from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from.models import Task
from .forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'
class Taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'
class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})

# Create your views here.
def home(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        Name=request.POST.get('name','')
        Priority=request.POST.get('priority','')
        Date=request.POST.get('date','')
        tasks=Task(name=Name,priority=Priority,date=Date)
        tasks.save()
        return redirect('/')
    return render(request,"home.html",{'task1':task1})

def delete(request,taskid):
     task2=Task.objects.get(id=taskid)
     if request.method=='POST':
         task2.delete()
         return redirect('/')
     return render(request,'delete.html')

def update(request,id):
    task= Task.objects.get(id=id)
    f=todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f ,'task':task })