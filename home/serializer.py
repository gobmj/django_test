from django.contrib.auth.models import User, Group

from rest_framework import serializers
from .models import Todo

# first we define the serializers



class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('title','description','user')

