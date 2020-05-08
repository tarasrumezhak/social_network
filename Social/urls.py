from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework import routers
from users.api.views import UserViewSet
from feed.api.views import PostViewSet, LikeView
from rest_framework_simplejwt import views as jwt_views


from feed import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
# router.register(r'analytics', LikeView, basename='like_view')
# router.register(r'analytics')

urlpatterns = [
    re_path(r'^users/', include(('users.urls', 'users'), namespace='users')),
    path(r'', include(('feed.urls', 'feed'), namespace='feed')),
    path('api/', include(router.urls)),
    path('api/analytics/', LikeView.as_view({'get': 'list'})),
    path('admin/', admin.site.urls),
    path(r'like/', views.like_post, name='like_post'),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)