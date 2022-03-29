from datetime import date, datetime, timedelta
import json
from django.contrib.auth.decorators import login_required
from unicodedata import category
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView,DeleteView
from django.shortcuts import render,redirect
from main.forms import AddTaskForm

from main.models import ToDoList

def home(request):
    form = AddTaskForm()
    items_today = ToDoList.objects.filter(date_end = str(date.today()))
    if request.user.is_authenticated:
        items = ToDoList.objects.filter(author=request.user, completed=False)
        el = ToDoList.objects.all()
    else:
        items = None
    if request.method == 'GET':
        id_list= request.GET.getlist('completed')
        for x in id_list:
            ToDoList.objects.filter(pk=int(x)).update(completed=True, date_completed=datetime.now())
            return redirect("home")
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            ToDoList.objects.create(**form.cleaned_data, author=request.user, date_created=datetime.now())
            return redirect('home')      
        items = ToDoList.objects.filter(author=request.user)

    return render(request, 'main/index.html', {'form': form,  'items_today':items_today, 'items': items})

class CompletedTasks(ListView):
    model = ToDoList
    template_name = 'main/completed.html'
    def get_context_data(self,**kwargs):
        items = ToDoList.objects.filter(completed="True")
        context = super().get_context_data(**kwargs)
        days_left = []
        for item in items:
            item_days_left = ((item.date_completed + timedelta(days=30)) - date.today()).days
            if item_days_left <= 0:
                    item.delete()
        context['items'] = items
        context['days_left'] = days_left
        return context



class TaskEditJS(View):
    def post(self, request):
        data = json.loads(request.body)
        obj = ToDoList.objects.get(pk=data.get('pk'))
        obj.completed = data.get('value')
        obj.date_completed = datetime.now()
        obj.save()
        return JsonResponse({"success": True})

def DeleteTask(request,id):
    obj = ToDoList.objects.filter(id=id)
    if request.user == obj.first().author:
        obj.delete()
        return redirect('completed')
    else:
        pass #TODO handle 404Error

def DeleteAll(request):
    ToDoList.objects.filter(author=request.user).delete()
    return redirect('completed')

    #TODO divide main page by today tomorrow and later