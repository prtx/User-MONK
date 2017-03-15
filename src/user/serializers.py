from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Monk


class CreateUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']


class CreateMonkSerializer(serializers.ModelSerializer):

	user = CreateUserSerializer()

	class Meta:
		model = Monk
		fields = ['user']

	def create(self, validated_data):
		
		user = User()
		user.username = validated_data['user']['username']
		user.email = validated_data['user']['email']
		user.password = validated_data['user']['password']
		user.save()

		monk = Monk(user=user)
		monk.save()

		return monk


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']


class MonkSerializer(serializers.ModelSerializer):

	user = UserSerializer()

	class Meta:
		model = Monk
		fields = ['user', 'image']