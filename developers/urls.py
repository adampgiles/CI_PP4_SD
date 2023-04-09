
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_developers, name='developers'),
    path('<developer_id>', views.developer_profile, name='developer_profile'),
    path('add/', views.add_developer, name='add_developer'),
    path('edit/<int:developer_id>/', views.edit_developer, name='edit_developer'),
    path('delete/<int:developer_id>/', views.delete_developer, name='delete_developer'),
    path('post/<int:developer_id>/', views.add_post, name='add_post'),
]
