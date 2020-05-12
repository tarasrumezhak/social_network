from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from feed.forms import CreateBlogPostForm
from feed.models import Post, Like


def index(request):
    """Home page of the social network"""
    return render(request, "feed/index.html")


@login_required(login_url='users:login')
def posts(request):
    """Representation of all posts"""
    posts = Post.objects.order_by('-publication_date')
    context = {'posts': posts}
    return render(request, 'feed/posts.html', context)


@login_required(login_url='users:login')
def post(request, post_id):
    """Representation of one post"""
    post = Post.objects.get(id=post_id)
    # likes = post.entry_set.order_by('-date_added')
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {'post': post, 'is_liked': is_liked, 'likes_count': post.likes_count()}
    return render(request, 'feed/post.html', context)


@login_required(login_url='users:login')
def new_post(request):
    """Create a new post"""
    context = {}
    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = request.user
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()
        return HttpResponseRedirect(reverse('feed:posts'))

    context['form'] = form

    return render(request, "feed/new_post.html", context)


@login_required(login_url='users:login')
def like_post(request):
    """Like the post"""
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        Like.objects.filter(post=post, user=request.user).delete()
        is_liked = False
    else:
        post.likes.add(request.user)
        Like.objects.create(post=post, user=request.user)
        is_liked = True
    return HttpResponseRedirect(request.META['HTTP_REFERER'])