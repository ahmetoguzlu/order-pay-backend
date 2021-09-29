# from django.shortcuts import render
from rest_framework import viewsets
from menu.models import Section, Item
from menu.serializers import SectionSerializer, ItemSerializer

class SectionViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = SectionSerializer
	queryset = Section.objects.all()

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = ItemSerializer
	
	def get_queryset(self):
		"""
		Returns items in the section
		"""

		queryset = Item.objects.all()
		section = self.request.query_params.get('section')
		if section is not None:
			queryset = queryset.filter(section=section)
		return queryset