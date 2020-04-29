from django.urls import path
from .views import (
    LabListView,
    DiagramsListView,
    ZingChartListView,
    ChartJSListView,
    )

urlpatterns = [
    path('', LabListView.as_view(), name='lab-home'),
    path('diagrams/', DiagramsListView.as_view(), name='diagrams-home'),
    path('diagrams/zingchart/', ZingChartListView.as_view(), name='diagrams-zingchart'),
    path('diagrams/chartjs', ChartJSListView.as_view(), name='diagrams-chartjs'),
]