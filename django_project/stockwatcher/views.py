from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Stock
import yfinance as yf
from django.http import JsonResponse
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
  paginate_by = 1

  # def get_context_data(self, *args, **kwargs):
  #   # Call the base implementation first to get a context 
  #   tickerData = yf.Ticker("AAPL")
  #   tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
  #   context = super().get_context_data(*args,**kwargs)
  #   context['date'] = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
  #   context['stockprice'] =  tickerDf.Close.values.tolist()
  #   return JsonResponse(context)

def about(request):
  return render(request, 'stockwatcher/about.html', {'title': 'About'})

def contact(request):
  return render(request, 'stockwatcher/contact.html', {'title': 'Contact'})