from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CutomUserCreationForm

# Create your views here.
class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = CutomUserCreationForm
    success_url = reverse_lazy("accounts:singup_success")


class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"