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


class StockGraphView(ListView):
  model = Stock
  template_name = 'stockwatcher/graphs.html'
  context_object_name = 'stocks'


def about(request):
  return render(request, 'stockwatcher/about.html', {'title': 'About'})


def stock_list(request):
  stock_list = Stock.objects.all()
  page_number = request.GET.get('page', 1)
  paginate_result = do_paginate(stock_list, page_number)
  stock_list_pagination_results = paginate_result[0]
  paginator = paginate_result[1]
  base_url = "/stocks?"
  return render(request, 'stockwatcher/stocks.html', {'base_url': base_url, 'stock_list': stock_list_pagination_results, 'paginator': paginator})

def stock_search(request):
  ticker = request.POST.get('ticker', '').strip()
  if len(ticker) == 0:
    ticker = request.GET.get('ticker').strip()

  stock_list = Stock.objects.filter(ticker__contains=ticker)
  page_number = request.GET.get('page', 1)
  paginate_result = do_paginate(stock_list, page_number)
  stock_list_pagination_results = paginate_result[0]
  paginator = paginate_result[1]
  base_url = f"/stock_search?ticker={ticker}"
  return render(request, 'stockwatcher/stocks.html', {'base_url': base_url, 'stock_list': stock_list_pagination_results, 'paginator': paginator, 'search_ticker': ticker})


def do_paginate(data_list, page_number):
    ret_data_list = data_list
    # suppose we display at most 2 records in each page.
    result_per_page = 9
    # build the paginator object.
    paginator = Paginator(data_list, result_per_page)
    try:
        # get data list for the specified page_number.
        ret_data_list = paginator.page(page_number)
    except EmptyPage:
        # get the lat page data if the page_number is bigger than last page number.
        ret_data_list = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # if the page_number is not an integer then return the first page data.
        ret_data_list = paginator.page(1)
    return [ret_data_list, paginator]