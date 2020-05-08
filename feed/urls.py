from django.urls import path, re_path, include

from . import views

urlpatterns = [
    # Home page
    path(r'', views.index, name='index'),
    # path(r'api/', include(('feed.api.urls', 'api'), namespace='api')),
    path(r'posts/', views.posts, name='posts'),
    path(r'posts/<int:post_id>/', views.post, name='post'),
    path('new_post/', views.new_post, name='new_post'),
]

# path(r'posts/(?P<post_id>\d+)/', views.post, name='post'),
