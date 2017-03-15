from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Monk
from .serializers import MonkSerializer

# Create your views here.

class Monk_ListAPIView(ListAPIView):

	queryset = Monk.objects.all()
	serializer_class = MonkSerializer


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