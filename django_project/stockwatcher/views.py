from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Stock
# Create your views here.


def home(request):
    context = {}
    return render(request, 'stockwatcher/home.html', context)

class StockListView(ListView):
  model = Stock
  template_name = 'stockwatcher/home.html' # <app>/<model>_<viewtype>.html
  context_object_name = 'stocks'
  ordering = ['id']
  paginate_by = 500

class StockGraphView(ListView):
  model = Stock
  template_name = 'stockwatcher/graphs.html'
  context_object_name = 'stocks'

def about(request):
  return render(request, 'stockwatcher/about.html', {'title': 'About'})

def contact(request):
  return render(request, 'stockwatcher/contact.html', {'title': 'Contact'})