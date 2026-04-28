from django.forms.models import modelform_factory
from django.shortcuts import render, redirect

from forum.forms import PostCreateForm, PostDeleteForm, SearchForm, CommentForm, CommentFormSet
from forum.models import PostBaseModel

def index(request):
    return render(request,'index.html')


def dashboard(request):
    search_form = SearchForm(request.GET)
    posts = PostBaseModel.objects.all()

    if request.method == "GET" and search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        posts = posts.filter(
            title__icontains=query
        )

    context={
        'posts':posts,
        'search_form':search_form
    }

    return render(request, 'dashboard.html',context)


def post_create_view(request):
    form = PostCreateForm(request.POST or None,request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request,'create-post.html',context)


def post_edit_form(request,pk):
    post = PostBaseModel.objects.get(pk=pk)

    if request.user.is_superuser:
        PostEditForm = modelform_factory(PostBaseModel, fields='__all__')
    else:
        PostEditForm = modelform_factory(PostBaseModel, fields=('context',))

    form = PostEditForm(request.POST or None, instance=post )

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form':form
    }

    return render(request,'edit-post.html',context)

def post_details_view(request, pk):
    post = PostBaseModel.objects.get(pk=pk)


    formset = CommentFormSet(request.POST or None)

    if request.method=="POST" and formset.is_valid():
        for form in formset:
            comment = form.save(commit=False)
            comment.author = request.user.username
            comment.post = post
            comment.save()
        return redirect('detail-post',pk=post.pk)

    context={
        'post':post,
        'formset':formset
    }

    return render(request,'post-details.html',context)


def post_delete_view(request,pk):
    post = PostBaseModel.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')

    context={
        'form':form
    }

    return render(request,'delete-post.html',context)












