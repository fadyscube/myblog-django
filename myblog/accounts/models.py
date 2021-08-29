from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	birthday = models.DateField()
	phonenumber = models.IntegerField()

	def __str__(self):
		return self.user.username
