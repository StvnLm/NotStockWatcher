from django.urls import path
from . import views
from .views import StockListView

# urlpatterns = [  path('home/', views.home, name = "stockwatcher-home")]

urlpatterns = [  path('home/', StockListView.as_view(), name = "stockwatcher-home")]