from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
# Create your views here.

class IndexView(TemplateView):
    
    template_name = 'app_name/pages/page_demo01.html'

