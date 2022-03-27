from rest_framework import serializers
from Items.models import Items

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"