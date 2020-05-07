from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse

from feed.forms import CreateBlogPostForm
from feed.models import Post, upload_location


def index(request):
    """Home page of the learning log application"""
    return render(request, "feed/index.html")


@login_required(login_url='users:login')
def posts(request):
    posts = Post.objects.order_by('-publication_date')
    context = {'posts': posts}
    return render(request, 'feed/posts.html', context)


@login_required(login_url='users:login')
def post(request, post_id):
    """Renders one topic and all it's entries"""
    post = Post.objects.get(id=post_id)
    # likes = post.entry_set.order_by('-date_added')
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {'post': post, 'is_liked': is_liked, 'likes_count': post.likes_count()}
    return render(request, 'feed/post.html', context)

# @login_required(login_url='users:login')
# def new_post(request):
#     """Creates new topic"""
#     if request.method != 'POST':
#         # Data is not sent, creates emply form
#         form = CreateBlogPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             return HttpResponseRedirect(reverse('feed:posts'))
#     else:
#         # Sent POST data, process data
#         form = CreateBlogPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # new_post = form.save(commit=False)
#             # new_post.author = request.user
#             # file = request.FILES[0]
#             # fs = FileSystemStorage()
#             # filename = fs.save(file.name, file)
#             # uploaded_file_url = fs.url(filename)
#             # new_post.image = uploaded_file_url
#             # new_post.save()
#             form = CreateBlogPostForm()
#             # return HttpResponseRedirect(reverse('feed:posts'))
#
#     context = {'form': form}
#     return render(request, 'feed/new_post.html', context)


@login_required(login_url='users:login')
def new_post(request):
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
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(request.META['HTTP_REFERER'])