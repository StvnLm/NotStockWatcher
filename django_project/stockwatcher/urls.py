from django.urls import path
from . import views
from django_filters.views import FilterView
from .views import *

urlpatterns = [ path('', views.home, name="stockwatcher-home"),
                # path(r'^stocks$', FilterView.as_view(model=Stock, filterset_fields=['senator']), name="stockwatcher-stocks"),
                path(r'^stocks$', views.stock_search, name="stockwatcher-stocks"),
                path('graphs/', StockGraphView.as_view, name="stockwatcher-graph"),
                path('about/', views.about, name="stockwatcher-about")]

