# myproject/views.py
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from github import Github

from .forms import UserNameForm

import requests

from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter


class Home(TemplateView):
    template_name = 'index.html'