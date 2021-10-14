import django_filters
from .models import *

class SearchFilter(django_filters.FilterSet):

  class Meta:
    model = Stock
    fields = [
      'ticker',
      'asset_description',
      'asset_type',
      'amount',
      'type',
      'transaction_date',
      'senator',
    ]