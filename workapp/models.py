from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='tasks')
    due_date = models.DateField()

    def __str__(self):
        return self.title