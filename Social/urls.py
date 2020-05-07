from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from feed import views


urlpatterns = [
    re_path(r'^users/', include(('users.urls', 'users'), namespace='users')),
    path(r'', include(('feed.urls', 'feed'), namespace='feed')),
    path('admin/', admin.site.urls),
    path(r'^like/$', views.like_post, name='like_post'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)