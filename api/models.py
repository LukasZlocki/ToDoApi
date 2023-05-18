from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    metadata = models.CharField(max_length=50, unique=True)
    deadline = models.DateField()
    description = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title