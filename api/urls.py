from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),

    path('brands-list/', views.brandsList, name="brands-list"),
    path('brands-detail/<int:pk>/', views.brandsDetail, name="brands-detail"),
    path('brands-create/', views.brandsCreate, name="brands-create"),
    path('brands-update/<str:pk>/', views.brandsUpdate, name="brands-update"),
    path('brands-delete/<str:pk>/', views.brandsDelete, name="brands-delete"),

    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-create/', views.taskCreate, name="task-create"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),

    path('tbc-brands-count/', views.TobaccosByBrands.as_view(), name="brands-count"),
    path('wish-brands-count/', views.WishlistByBrands.as_view(), name="wish-brands-count"),
    path('inv-brands-count/', views.InventoryByBrands.as_view(), name="inv-brands-count"),
    path('wish-tbc-count/', views.WishlistByTobacco.as_view(), name="wish-tbc-count"),
    path('inv-tbc-count/', views.InventoryByTobacco.as_view(), name="inv-tbc-count"),
]
