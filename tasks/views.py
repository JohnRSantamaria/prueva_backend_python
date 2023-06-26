from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Taks
# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Taks.objects.all()