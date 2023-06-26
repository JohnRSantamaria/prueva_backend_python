from rest_framework import serializers
from .models import Taks


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taks
        # fields = ('id', 'title','description','done') 
        fields = '__all__'