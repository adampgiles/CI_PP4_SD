from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.contact_us, name='contact_us'),
]