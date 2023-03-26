from django.contrib import admin
from .models import Developer
from .models import Category

# Register your models here.
admin.site.register(Developer)
admin.site.register(Category)