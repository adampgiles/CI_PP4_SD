
from django.urls import path
from . import views

urlpatterns = [
    path('my_account/', views.user_account, name='user_account'),
]
