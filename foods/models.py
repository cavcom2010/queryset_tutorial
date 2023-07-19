from django.db import models

class Food(models.Model):
	name = models.TextField()
	color = models.TextField()

	def __str__(self):
		return self.name
		
