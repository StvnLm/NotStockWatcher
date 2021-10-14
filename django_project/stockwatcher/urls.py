from django.urls import path
from . import views
from .views import StockListView, StockGraphView

urlpatterns = [ path('', views.home, name = "stockwatcher-home"),
                path('stocks/', StockListView.as_view(), name = "stockwatcher-stocks"),
                path('search/', views.search, name='search-results'),
                path('graphs/', StockGraphView.as_view(),name="stockwatcher-graph"),
                path('about/', views.about, name = "stockwatcher-about")]

