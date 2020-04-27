from rest_framework import serializers
from tobacco.models import Brands, TobaccoList, Inventory, Wishlist


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'
