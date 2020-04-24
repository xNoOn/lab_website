from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Brands, TobaccoList, Inventory, Wishlist


class BrandsForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ['Brand', 'Price', 'Weight', 'Image']


class TobaccoForm(forms.ModelForm):
    class Meta:
        model = TobaccoList
        fields = ['BrandID', 'Name', 'Taste', 'Inventory', 'Wish', 'Comment', 'Image', 'QTaste', 'QSmoke', 'QCut']


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['TobaccoID', 'Quantity']


class WishForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['TobaccoID', 'Priority']