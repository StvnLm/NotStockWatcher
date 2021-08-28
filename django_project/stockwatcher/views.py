from django.shortcuts import render
from django.views.generic import ListView
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
#   paginate_by = 100
