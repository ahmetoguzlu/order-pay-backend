from rest_framework import serializers
from menu.models import Section, Item, ItemOptionBinary, ItemOptionSelection

class SectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Section
		fields = ['name', 'img', 'order_num']

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ['section', 'name', 'img', 'description', 'price']

class ItemOptionBinarySerializer(serializers.ModelSerializer):
	class Meta:
		model = ItemOptionBinary
		fields = ['item', 'name']

class ItemOptionSelectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = ItemOptionSelection
		fields = ['item', 'name', 'options']