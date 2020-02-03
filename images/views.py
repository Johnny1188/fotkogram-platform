from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Like, Comment
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url="/crossroad")
def home(request):
    posts_objects = Post.objects.order_by('-pub_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_objects, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'images/home.html', {'posts': posts})

def crossroad(request):
    return render(request, 'images/crossroad.html')

@login_required(login_url="/crossroad")
def createpost(request):
    if request.method == 'POST':
        if request.POST['text'] and request.FILES['image']:
            new_post = Post()
            new_post.image = request.FILES['image']
            new_post.text = request.POST['text']
            new_post.pub_date = timezone.datetime.now()
            new_post.publisher = request.user
            new_post.save()
            return redirect('home')
        else:
            return render(request, 'images/createpost.html', {'error': 'Add an image and add something'})
    else:
        return render(request, 'images/createpost.html')

@login_required(login_url="/crossroad")
def like(request, posts_id, liker_id):
    if request.method == 'POST':
        liker = request.user
        post = Post.objects.get(pk=posts_id)
        try:
            like = Like.objects.get(liker=liker, post=post)
            return redirect('/')
        except Like.DoesNotExist:
            new_like = Like()
            new_like.liker = liker
            new_like.post = post
            new_like.save()
            post.number_of_likes += 1
            post.save()
            return redirect('/')
    else:
        return render(request, 'images/crossroad.html')

@login_required(login_url="/crossroad")
def comment(request, posts_id, commenter_id):
    if request.method == 'POST':
        if request.POST["comment_text"]:
            commenter = User.objects.get(pk=commenter_id)
            post = Post.objects.get(pk=posts_id)
            new_comment = Comment()
            new_comment.commenter = commenter
            new_comment.post = post
            new_comment.pub_date = timezone.datetime.now()
            new_comment.text = request.POST["comment_text"]
            new_comment.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return render(request, 'images/crossroad.html')