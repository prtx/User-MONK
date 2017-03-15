from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Monk(models.Model):

	user = models.OneToOneField(User)
	image = models.FileField(upload_to='display_picture', null=True)

	def __str__(self):
		return self.user.username


class Activity(models.Model):

	monk = models.ForeignKey(Monk)
	timestamp = models.DateTimeField()
	short_desc = models.CharField(max_length=500)
	long_desc = models.TextField()