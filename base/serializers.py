from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
     class Meta:
         model = Task
         fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = 'id', 'last_login', 'is_superuser', 'username', 'date_joined'