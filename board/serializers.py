from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Board

class BoardSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Board
        fields = "__all__"

class RegisterUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
