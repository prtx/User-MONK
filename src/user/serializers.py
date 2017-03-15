from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Monk

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email']

class MonkSerializer(serializers.ModelSerializer):

	user = UserSerializer(read_only=False)

	class Meta:
		model = Monk
		fields = ['user', 'image']