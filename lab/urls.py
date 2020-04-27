from django.urls import path
from .views import (
    LabListView,
    DiagramsListView
    )

urlpatterns = [
    path('', LabListView.as_view(), name='lab-home'),
    path('diagrams/', DiagramsListView.as_view(), name='diagrams-home'),

]