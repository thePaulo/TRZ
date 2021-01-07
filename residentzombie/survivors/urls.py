from django.urls import path
from . import views

app_name = "survivors"
urlpatterns = [
    path("<int:survivor_id>/trading",views.displayTrades),
    #path("<int:survivor_id>/trading/processing",views.processTrades),
]
