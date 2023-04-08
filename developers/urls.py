
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_developers, name='developers'),
    path('<developer_id>', views.developer_profile, name='developer_profile'),
    path('add/', views.add_developer, name='add_developer'),
]
