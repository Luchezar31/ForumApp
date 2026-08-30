from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms.models import modelform_factory, model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, ListView, CreateView, DeleteView, DetailView
from django.views.generic.edit import FormMixin

from forum.forms import PostCreateForm, PostDeleteForm, SearchForm, CommentFormSet
from forum.mixins import TimeRestrictionMixin
from forum.models import PostBaseModel

def index(request):
    return render(request,'index.html')

class IndexView(View):

    def get(self,request,*args,**kwargs):
        return render(request,'index.html')

def approve_view(request,pk):
    post = PostBaseModel.objects.get(pk=pk)
    post.approved=True
    post.save()

    return redirect('dashboard')

class DashboardView(ListView,PermissionRequiredMixin):
    template_name = 'dashboard.html'
    model = PostBaseModel
    context_object_name = 'posts'
    paginate_by = 5
    permission_required = 'posts.can_approve_post'

    def get_queryset(self):

        queryset = super().get_queryset().order_by('-created_at')

        self.form = SearchForm(self.request.GET)

        if not self.has_permission():
            queryset = queryset.filter(approved=True)


        if self.form.is_valid():
            query = self.form.cleaned_data.get('query')
            if query:
                queryset = queryset.filter(title__icontains=query)

        return queryset

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if hasattr(self, 'form') and self.form.is_valid():
            query = self.form.cleaned_data.get('query')
            if query:
                context['query'] = query

        return context


class PostCreateView(LoginRequiredMixin,TimeRestrictionMixin, CreateView):
    form_class = PostCreateForm
    template_name = 'create-post.html'
    success_url = reverse_lazy('dashboard')


class EditPostView(UpdateView):
    model = PostBaseModel
    template_name = 'edit-post.html'
    success_url = reverse_lazy('dashboard')

    def get_form_class(self):
        if self.request.user.is_authenticated:
            return modelform_factory(PostBaseModel,fields='__all__')
        return modelform_factory(PostBaseModel,fields=('context',))



class PostDetailView(DetailView, FormMixin):
    template_name = 'post-details.html'
    model = PostBaseModel
    context_object_name = 'post'
    form_class = CommentFormSet

    def get_context_data(self,**kwargs):

        kwargs = super().get_context_data(**kwargs)

        kwargs.update({'formset': self.get_form_class()()})

        return kwargs

    def get_success_url(self,*args,**kwargs):
        return reverse_lazy('detail-post',kwargs={'pk':self.kwargs.get(self.pk_url_kwarg)})

    def post(self,*args,**kwargs):
        self.object = self.get_object()
        formset = self.form_class(self.request.POST)

        if formset.is_valid():
            for form in formset:
                comment = form.save(commit=False)
                comment.author = self.request.user.username
                comment.post = self.object
                comment.save()

        return HttpResponseRedirect(self.get_success_url())


class DeletePostView(DeleteView):
    form_class = PostDeleteForm
    model = PostBaseModel
    success_url = reverse_lazy('dashboard')
    template_name = 'delete-post.html'

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = PostBaseModel.objects.get(pk=pk)
        return model_to_dict(post)

    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()

        if self.request.method == 'POST':
            kwargs['data'] = self.get_initial()
        return kwargs












