from django.urls import path
from . import views
from .views import StockListView, StockGraphView

urlpatterns = [ path('', views.home, name = "stockwatcher-home"),
                path('stocks/', StockListView.as_view(), name = "stockwatcher-stocks"),
                path('graphs/', StockGraphView.as_view(),name="stockwatcher-graph"),
                path('about/', views.about, name = "stockwatcher-about"),
                path('contact/', views.contact, name = "stockwatcher-contact"),]

