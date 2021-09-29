from rest_framework import serializers
from menu.models import Section, Item

class SectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Section
		fields = ['name', 'img', 'order_num']

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ['section', 'name', 'img', 'description', 'price', 'options_binary', 'options_selection']