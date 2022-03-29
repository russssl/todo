# def home(request):
#     form = AddTaskForm()
#     if request.user.is_authenticated:
#         items = ToDoList.objects.filter(author=request.user, completed=False)
#         el = ToDoList.objects.all()
#     else:
#         items = None
#     if request.method == 'GET':
#         id_list= request.GET.getlist('completed')
#         for x in id_list:
#             ToDoList.objects.filter(pk=int(x)).update(completed=True, date_completed=datetime.now())
#             return redirect("home")
#     if request.method == 'POST':
#         if request.POST.get("save"):
#             el.save()
#         form = AddTaskForm(request.POST)
#         if form.is_valid():
#             ToDoList.objects.create(**form.cleaned_data, author=request.user, date_created=datetime.now())
#             return redirect('home')      
#         items = ToDoList.objects.filter(author=request.user)
#     return render(request, 'main/home.html', {'form': form, 'items': items})