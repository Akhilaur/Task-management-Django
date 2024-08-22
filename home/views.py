from django.shortcuts import render,redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Tasks
from.forms import todoform

# Create your views here.

def index(request):
    todo = Tasks.objects.all()    
    if request.method == 'POST':
        form=todoform(request.POST)
        if form.is_valid():
            instance = form.save(commit=True)
            instance.save()
            return redirect('index')
    else:
        form=todoform()
    context={'todo':todo,'form':form}
    return render(request, 'index.html',context)

def update(request,pk):
    todo=Tasks.objects.get(id=pk)
    form=todoform(instance=todo)
    if request.method=='POST':
       form= todoform(request.POST,instance=todo)
       if form.is_valid():
            instance = form.save(commit=True)
            instance.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'update.html', context)
    
def delete(request,pk):
    try:
      todo=Tasks.objects.get(id=pk)
      todo.delete()
      return redirect('index')
    except Tasks.DoesNotExist:
        return HttpResponse('task not found',status=404)
    
def completed(request,pk):
    todo=Tasks.objects.get(pk=pk)
    todo.completed=True
    todo.save()
    return redirect('index')

def uncompleted(request,pk):
    todo=Tasks.objects.get(pk=pk)
    todo.completed=False
    todo.save()
    return redirect('index')


    





    


    


