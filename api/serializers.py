from rest_framework import serializers
from tobacco.models import Brands, TobaccoList, Inventory, Wishlist, Task


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
