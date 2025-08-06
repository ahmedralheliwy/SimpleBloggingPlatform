from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.all().order_by('-created_at')
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context={
        'form':form,
        'posts': posts
    }
    return render(request,'index.html',context)

def edit_post(request, post_id): 
    post= Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'edit.html', context)

def delete_post(request, post_id):
    if request.method == "DELETE":
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        return HttpResponse('')
    else:
        return HttpResponse(status=405)