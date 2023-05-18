from rest_framework import serializers
from .models import Task

# this model turns data into json model

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')
