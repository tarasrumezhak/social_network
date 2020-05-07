from django.urls import path, re_path

from . import views

urlpatterns = [
    # Home page
    path(r'', views.index, name='index'),
    path(r'posts/', views.posts, name='posts'),
    path(r'posts/(?P<post_id>\d+)/', views.post, name='post'),
    path('new_post/', views.new_post, name='new_post'),
]