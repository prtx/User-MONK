from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Monk
from .serializers import CreateMonkSerializer, MonkSerializer

# Create your views here.

class Monk_ListAPIView(ListAPIView):

	queryset = Monk.objects.all()
	serializer_class = MonkSerializer


class Monk_CreateAPIView(CreateAPIView):

	queryset = Monk.objects.all()
	serializer_class = CreateMonkSerializer


class Monk_DetailAPIView(RetrieveAPIView):

	queryset = Monk.objects.all()
	serializer_class = MonkSerializer
	lookup_field = 'user'


class Monk_UpdateAPIView(UpdateAPIView):

	queryset = Monk.objects.all()
	serializer_class = MonkSerializer
	lookup_field = 'user'


class Monk_DeleteAPIView(DestroyAPIView):

	queryset = Monk.objects.all()
	serializer_class = MonkSerializer
	lookup_field = 'user'