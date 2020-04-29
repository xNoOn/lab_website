from django.db import models
from django.utils import timezone
from PIL import Image


class Brands(models.Model):
    # BrandID = models.AutoField(primary_key=True)
    Brand = models.CharField(max_length=64, unique=True)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Weight = models.DecimalField(max_digits=4, decimal_places=0)
    Image = models.ImageField(default='tobacco_default.png', upload_to='brand_pics')

    def __str__(self):
        return f'{self.Brand}'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


class TobaccoList(models.Model):
    quality_choices = (
        ('?', '?'),
        ('Sehr Gut', 'Sehr Gut'),
        ('Gut', 'Gut'),
        ('Befriedigend ', 'Befriedigend '),
        ('Ausreichend ', 'Ausreichend '),
        ('Mangelhaft ', 'Mangelhaft '),
        ('Ungenügend', 'Ungenügend'),
    )

    # TobaccoID = models.AutoField(primary_key=True)
    Brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    Name = models.CharField(max_length=64)
    Taste = models.CharField(max_length=64)
    Comment = models.TextField(null=True, blank=True)
    Date_Posted = models.DateTimeField(default=timezone.now)
    Image = models.ImageField(default='tobacco_default.png', upload_to='tobacco_pics')

    QTaste = models.CharField(max_length=16, choices=quality_choices, default='?')
    QSmoke = models.CharField(max_length=16, choices=quality_choices, default='?')
    QCut = models.CharField(max_length=16, choices=quality_choices, default='?')

    Inventory = models.BooleanField(default=True)
    Wish = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.Name}  [{self.Brand.Brand}] '

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.Image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.Image.path)


# Inventory Model
class Inventory(models.Model):
    quantity_choices = (
        (0, '0%'),
        (10, '10%'),
        (20, '20%'),
        (30, '30%'),
        (40, '40%'),
        (50, '50%'),
        (60, '60%'),
        (70, '70%'),
        (80, '80%'),
        (90, '90%'),
        (100, '100%'),
    )

    # InventoryID = models.AutoField(primary_key=True)
    Tobacco = models.OneToOneField(TobaccoList, on_delete=models.CASCADE)
    Quantity = models.IntegerField(choices=quantity_choices, default=100)

    def __str__(self):
        return f'{self.Tobacco.Brand.Brand} - {self.Tobacco.Name} : {self.Tobacco.Inventory}'


# Wishlist Model
class Wishlist(models.Model):
    wish_choices = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )

    # WishlistID = models.AutoField(primary_key=True)
    Tobacco = models.OneToOneField(TobaccoList, on_delete=models.CASCADE)
    Priority = models.CharField(max_length=8, choices=wish_choices, default='Medium')

    def __str__(self):
        return f'{self.Tobacco.Brand.Brand} - {self.Tobacco.Name} : {self.Tobacco.Wish}'


# API Test Model
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title
