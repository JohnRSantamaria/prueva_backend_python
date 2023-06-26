from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Taks
from django.http import HttpResponse
# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Taks.objects.all()

def login_view(request):
    return HttpResponse("<h1>Deployed</h1>")