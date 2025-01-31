from django.db import models

# Create your models here.
class Tasks(models.Model):
    task=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    completiondate=models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.task
    
    class Meta:
        ordering=['-completiondate']
