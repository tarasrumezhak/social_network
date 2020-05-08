from rest_framework import serializers

from feed.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'title', 'image', 'text', 'publication_date', 'author', 'likes')
