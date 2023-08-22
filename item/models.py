from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    Category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="items")
    name= models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="items_images", blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(auto_created=False)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name


