from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    
class Developer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=254)
    description = models.TextField(max_length=508)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count_sold = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.profile_name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Developer', on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.CharField(max_length=1000)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title