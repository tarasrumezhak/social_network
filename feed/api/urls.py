# from django.urls import include, path
# from rest_framework import routers
# from feed.api.views import PostViewSet, LikeView
#
# router = routers.DefaultRouter()
# router.register(r'posts/', PostViewSet)
# router.register(r'analytics/', LikeView.as_view())
#
# app_name = 'feed_api'
#
# urlpatterns = [
#     path('', include(router.urls)),
#     # path(r'', PostViewSet, name='detail'),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]