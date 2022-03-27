from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from api.serializers import ItemsSerializer
from Items.models import Items
# Create your views here.

class ListItemAPIView(ListAPIView):
     # This endpoint allows for list an todo items
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class CreateItemAPIView(CreateAPIView):
      # This endpoint allows for create an todo item
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    

class UpdateItemAPIView(UpdateAPIView):
    # This endpoint allows for updating an todo item
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class DeleteItemAPIView(DestroyAPIView):
     # This endpoint allows for delete an todo item
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    