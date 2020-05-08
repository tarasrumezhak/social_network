from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from feed.models import Post
from rest_framework import viewsets, status
from rest_framework import permissions
from feed.api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

# class AnalyticsViewSet(viewsets.ModelViewSet):
#     queryset =

# @api_view(['GET', ])
# @permission_classes((IsAuthenticated,))
# def api_detail_post_view(request, slug):
#     try:
#         post = Post.objects.get(slug=slug)
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
