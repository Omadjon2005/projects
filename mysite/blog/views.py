from django.shortcuts import render,redirect
from blog.models import PostModel
from .forms import PostModelForm,PostUpdateForm,CommentForm


def home(request):
    data=PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home-page')
    else:
        form = PostModelForm()
    context={
        'posts':data,
        'form':form
    }
    return render(request,'home.html',context)



def post_detail(request,pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('post_detail-page',pk=post.id)
    else:
        c_form = CommentForm()
    context = {
        'post': post,
        'c_form':c_form,
    }
    return render(request,'post_detail.html',context)


def post_edit(request,pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail-page',pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post':post,
        'form':form,
    }
    return render(request, 'post_edit.html',context)


def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home-page')
    context = {
        'post':post
    }
    return render(request,'post_delete.html',context)












