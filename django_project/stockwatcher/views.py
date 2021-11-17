from typing import List
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q # new
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Stock
from .filters import StockFilter
import requests

def home(request):
  return render(request, 'stockwatcher/home.html', {'title': 'Home'})

# class StockListView(ListView):
#   model = Stock
#   template_name = 'stockwatcher/stocks.html' # <app>/<model>_<viewtype>.html
#   context_object_name = 'stocks'
#   ordering = ['id']
#   paginate_by = 30

class StockGraphView(ListView):
  model = Stock
  template_name = 'stockwatcher/graphs.html'
  context_object_name = 'stocks'

def about(request):
  return render(request, 'stockwatcher/about.html', {'title': 'About'})

def stock_search(request):
  f = StockFilter(request.GET, queryset=Stock.objects.all())
  return render(request, 'stockwatcher/search_results.html', {'filter': f})