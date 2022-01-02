from django.urls import path, re_path
from . import views
from django_filters.views import FilterView
from .views import *

urlpatterns = [ path('', views.home, name="stockwatcher-home"),
                path(r'stocks', views.stock_list, name="stockwatcher-stocks"),
                re_path(r'^stock_search/$', views.stock_search, name="stockwatcher-stocks-search"),
                path('about/', views.about, name="stockwatcher-about")]

