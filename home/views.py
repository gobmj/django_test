from django.shortcuts import render
from rest_framework import viewsets
from home.serializer import TodoSerializer
from home.models import Todo
# Create your views here.

def index(request):
    return render(request, "home/index.html")


class TodoSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    http_method_names = ['get','post','options','put']

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)