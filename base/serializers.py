from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
     def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Заголовок должен быть более 5 символов.")
        return value
     def validate_user(self, value):
        listA = [];
        if not len(listA):
            raise serializers.ValidationError("Выберите пользователя!")
        return value
     class Meta:
         model = Task
         fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = 'id', 'last_login', 'is_superuser', 'username', 'date_joined'