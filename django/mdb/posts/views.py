from re import template
from django.shortcuts import render
from django.views.generic.base import View, TemplateView

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

class Login2(View):
    def get(self, request):
        return render(request, 'login2.html')

class Login3(TemplateView):
    template_name = 'login3.html'
