from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=55)
	content = models.TextField()
	image = models.ImageField(upload_to='posts_image/')
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
