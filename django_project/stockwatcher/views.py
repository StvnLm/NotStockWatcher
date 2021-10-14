from typing import List
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Stock
from django.db.models import Q # new
from .filters import SearchFilter

# Create your views here.

def home(request):
  return render(request, 'stockwatcher/home.html', {'title': 'Home'})

class StockListView(ListView):
  model = Stock
  template_name = 'stockwatcher/stocks.html' # <app>/<model>_<viewtype>.html
  context_object_name = 'stocks'
  ordering = ['id']
  paginate_by = 30

class StockGraphView(ListView):
  model = Stock
  template_name = 'stockwatcher/graphs.html'
  context_object_name = 'stocks'

def about(request):
  return render(request, 'stockwatcher/about.html', {'title': 'About'})

def search(request):
  stock_list = Stock.objects.all()
  stock_filter = SearchFilter(request.GET, queryset=stock_list)
  return render(request, 'stockwatcher/search_results.html', {'stock': stock_filter})