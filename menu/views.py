# from django.shortcuts import render
from rest_framework import viewsets
from menu.models import Section, Item, ItemOptionBinary, ItemOptionSelection
from menu.serializers import SectionSerializer, ItemSerializer, ItemOptionBinarySerializer, ItemOptionSelectionSerializer

class SectionViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = SectionSerializer
	queryset = Section.objects.all()

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = ItemSerializer
	
	def get_queryset(self):
		"""
		Returns items in the current section
		"""

		queryset = Item.objects.all()
		section = self.request.query_params.get('section')
		if section is not None:
			queryset = queryset.filter(section=section)
		return queryset

class ItemOptionBinaryViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = ItemOptionBinarySerializer
	
	def get_queryset(self):
		"""
		Returns items in the current section
		"""

		queryset = ItemOptionBinary.objects.all()
		item = self.request.query_params.get('item')
		if item is not None:
			queryset = queryset.filter(item=item)
		return queryset

class ItemOptionSelectionViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = ItemOptionSelectionSerializer
	
	def get_queryset(self):
		"""
		Returns items in the current section
		"""

		queryset = ItemOptionSelection.objects.all()
		item = self.request.query_params.get('item')
		if item is not None:
			queryset = queryset.filter(item=item)
		return queryset