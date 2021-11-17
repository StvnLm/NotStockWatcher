import django_filters
from .models import *

class StockFilter(django_filters.FilterSet):
  senator = django_filters.CharFilter(field_name='senator' ,lookup_expr='icontains')
  ticker = django_filters.CharFilter(field_name='ticker', lookup_expr='iexact')
  
  class Meta:
    model = Stock
    exclude = [
      'asset_description',
      'asset_type',
      'amount',
      'type',
      'transaction_date',
    ]