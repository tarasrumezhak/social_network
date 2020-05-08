from django.db.models import Avg
from django.utils import timezone
from feed.models import Post, Like
from rest_framework import viewsets, status
from rest_framework import permissions
from feed.api.serializers import PostSerializer, LikeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class LikeView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer

    def get_queryset(self):
        date_from = self.request.GET.get('date_from', '2020-05-05')
        date_to = self.request.GET.get('date_to', timezone.now())
        post_id = int(self.request.GET.get('post_id', '0'))
        if post_id > 0:
            post = Post.objects.get(id=post_id)
            return Like.objects.filter(like_date__range=[date_from, date_to], post=post)
        else:
            return Like.objects.filter(like_date__range=[date_from, date_to])
