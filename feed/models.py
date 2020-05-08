from django.db import models
from django.contrib.auth.models import User


def upload_location(instance, filename):
    filepath = 'feed/photos/{author}/{title}-{filename}'.format(
        author=str(instance.author.username), title=str(instance.title), filename=filename
    )
    return filepath


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to=upload_location)
    text = models.CharField(max_length=2000, null=False, blank=False)
    publication_date = models.DateTimeField(auto_now=True, verbose_name="Publication Date")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    # likes = models.ManyToOneRel(Like, related_name='likes')

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes2")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post.title} : like from {self.user}'

