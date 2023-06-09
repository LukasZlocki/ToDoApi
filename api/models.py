from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    metadata = models.CharField(max_length=50)
    deadline = models.DateField()
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title