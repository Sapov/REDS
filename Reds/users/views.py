from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView

from .forms import CustomUserCreationForm
from .models import CustomUser


@login_required
def profile_view(request):
    return render(request, 'users/profile.html')


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

class CustomUserUpdateView(UpdateView): # Пользователь обновляет данные о себе
    model = CustomUser
    fields = ['phone', 'country']
    template_name_suffix = '_update_form'