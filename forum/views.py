from django.forms.models import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, ListView, CreateView, DeleteView, FormView

from forum.forms import PostCreateForm, PostDeleteForm, SearchForm, CommentFormSet
from forum.models import PostBaseModel

def index(request):
    return render(request,'index.html')

class IndexView(View):

    def get(self,request,*args,**kwargs):
        return render(request,'index.html')



class DashboardView(ListView):
    template_name = 'dashboard.html'
    model = PostBaseModel
    context_object_name = 'posts'

    def get_queryset(self):

        queryset = super().get_queryset()

        self.form = SearchForm(self.request.GET)

        if self.form.is_valid():
            query = self.form.cleaned_data.get('query')
            if query:
                queryset = queryset.filter(title__icontains=query)

        return queryset

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        return context

# def dashboard(request):
#     search_form = SearchForm(request.GET)
#     posts = PostBaseModel.objects.all()
#
#     if request.method == "GET" and search_form.is_valid():
#         query = search_form.cleaned_data.get('query')
#         posts = posts.filter(
#             title__icontains=query
#         )
#
#     context={
#         'posts':posts,
#         'search_form':search_form
#     }
#
#     return render(request, 'dashboard.html',context)


class PostCreateView(CreateView):
    form_class = PostCreateForm
    template_name = 'create-post.html'
    success_url = reverse_lazy('dashboard')

#
# def post_create_view(request):
#     form = PostCreateForm(request.POST or None,request.FILES or None)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('dashboard')
#
#     context = {
#         'form': form
#     }
#
#     return render(request,'create-post.html',context)


class EditPostView(UpdateView):
    model = PostBaseModel
    template_name = 'edit-post.html'
    success_url = reverse_lazy('dashboard')

    def get_form_class(self):
        if self.request.user.is_authenticated:
            return modelform_factory(PostBaseModel,fields='__all__')
        return modelform_factory(PostBaseModel,fields=('context',))


# def post_edit_form(request,pk):
#     post = PostBaseModel.objects.get(pk=pk)
#
#     if request.user.is_superuser:
#         PostEditForm = modelform_factory(PostBaseModel, fields='__all__')
#     else:
#         PostEditForm = modelform_factory(PostBaseModel, fields=('context',))
#
#     form = PostEditForm(request.POST or None, instance=post )
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('dashboard')
#
#     context = {
#         'form':form
#     }
#
#     return render(request,'edit-post.html',context)

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


class DeletePostView(DeleteView,FormView):
    form_class = PostDeleteForm
    model = PostBaseModel
    success_url = reverse_lazy('dashboard')
    template_name = 'delete-post.html'

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = PostBaseModel.objects.get(pk=pk)
        return post.__dict__

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












