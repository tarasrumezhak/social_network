from django.contrib.auth.models import User
from django.test import TestCase

from feed.models import Post, Like


class PostModelTests(TestCase):
    def test_post_representation(self):
        """Check the correctness of string representation"""
        post = Post(title="Test post")
        self.assertEquals(str(post), "Test post")