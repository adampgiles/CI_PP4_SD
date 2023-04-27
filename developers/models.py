from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


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
    user = models.OneToOneField(User, null=True, blank=True,
                                on_delete=models.SET_NULL)
    profile_name = models.CharField(max_length=254)
    description = models.TextField(max_length=508)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(0.00),
                                            MaxValueValidator(100.00)])
    count_sold = models.IntegerField(null=True, blank=True,
                                     validators=[MinValueValidator(0)])
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.profile_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Developer', null=True, blank=True,
                               on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.CharField(max_length=1000)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
