from django.urls import path
from . import views
from .views import StockListView, StockGraphView

# urlpatterns = [  path('home/', views.home, name = "stockwatcher-home")]
urlpatterns = [  path('', StockListView.as_view(), name = "stockwatcher-home"),
                path('graphs/', StockGraphView.as_view(),name="stockwatcher-graph"),
                path('about/', views.about, name = "stockwatcher-about"),
                path('contact/', views.contact, name = "stockwatcher-contact"),]

