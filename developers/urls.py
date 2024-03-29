from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_developers, name='developers'),
    path('<developer_id>', views.developer_profile, name='developer_profile'),
    path('add/', views.add_developer, name='add_developer'),
    path('edit/<int:developer_id>/', views.edit_developer,
         name='edit_developer'),
    path('confirmdelete/<int:developer_id>/', views.confirm_delete_developer,
         name='confirm_delete_developer'),
    path('delete/<int:developer_id>/', views.delete_developer,
         name='delete_developer'),
    path('addpost/<int:developer_id>/', views.add_post, name='add_post'),
    path('editpost/<int:post_id>/', views.edit_post, name='edit_post'),
    path('confirmdeletepost/<int:post_id>/', views.confirm_delete_post,
         name='confirm_delete_post'),
    path('deletepost/<int:post_id>/', views.delete_post, name='delete_post'),
]
