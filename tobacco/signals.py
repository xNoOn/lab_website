from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TobaccoList, Wishlist, Inventory


@receiver(post_save, sender=TobaccoList)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Inventory.objects.create(TobaccoID =instance)
        print('Inventory created!')

        Wishlist.objects.create(TobaccoID = instance)
        print('Wishlist created!')


