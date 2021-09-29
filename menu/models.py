from django.db import models
from django.contrib.postgres.fields import ArrayField

class Section(models.Model):
	ORDER_NUM_RANGE = 10
	name = models.CharField(max_length=100)
	img = models.ImageField(upload_to='images/', default='images/default.jpg')
	order_num = models.IntegerField(default=1, choices=zip(range(1,ORDER_NUM_RANGE), range(1,ORDER_NUM_RANGE)))

	def __str__(self):
		return self.name


class Item(models.Model):
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	img = models.ImageField(upload_to='images/', default='images/default.jpg')
	description = models.CharField(max_length=200, blank=True)
	price = models.FloatField(default=0.0)

	# Ex: ['pickles', 'tomato', 'vegan patty']
	options_binary = models.JSONField(default=list)

	# Ex: {'cooking': ['rare', 'medium', 'well-done']}
	options_selection = models.JSONField(default=dict)

	def __str__(self):
		return self.name
