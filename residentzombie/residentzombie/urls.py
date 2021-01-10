from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from survivors.api import viewsets as survivorsviewsets
from items.api import viewsets as itemsviewsets

from survivors import views as sview

route = routers.DefaultRouter()
route.register(r'survivors', survivorsviewsets.SurvivorsViewSet,basename="Survivors")
route.register(r'items', itemsviewsets.ItemsViewSet,basename="Items")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(route.urls)),
    path('trading',sview.displayTrades,name="trading"),
    path('reports',include("reports.urls"),name="reports")
]
