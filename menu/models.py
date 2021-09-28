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

	def __str__(self):
		return self.name


class ItemOptionBinary(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	# Option to have or not to have, i.e [pickles(yes/no), tomato(yes/no)] for a burger etc
	name = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.name


class ItemOptionSelection(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	# Make choice from a set, i.e [cook(rare,medium,well-done), side(salad, fries)] for steak
	name = models.CharField(max_length=100, blank=True)
	options = models.JSONField(default=list)

	def __str__(self):
		return str({self.name: self.options})
