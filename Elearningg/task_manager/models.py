from django.db import models
from django.contrib.auth.models import User

class Task_details(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=100)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    due_date = models.DateField()
    priority = models.CharField(
        max_length=10,
        choices=[
           ( 'Low' , 'Low'),
           ('Medium','Medium'),
           ('High','High')
        ]
    )
    isCompelete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title
    

