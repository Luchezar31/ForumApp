from django.contrib.auth import login
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import CustomUserCreationForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self,form):
        self.object = form.save()
        login(self.request,self.object,backend='accounts.backends.EmailBackend')
        return HttpResponseRedirect(self.get_success_url())


