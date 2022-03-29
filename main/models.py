from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ToDoList(models.Model):
    class Meta:
        verbose_name = "Task"
    name = models.CharField(max_length=70)
    task_body = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    
    date_end = models.DateTimeField(null=True, blank=True)
    date_created = models.DateField()
    date_completed = models.DateField(null=True,blank=True)

    def __str__(self):
        if self.completed:
            return self.name + " completed"
        else:
            return self.name + " uncompleted" 

#TODO add a end date functionality