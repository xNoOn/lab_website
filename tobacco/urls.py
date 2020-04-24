from users import views as user_views
from django.urls import path
from tobacco.views import (
    TobaccoOverviewView,
    TobaccoListDetailView,
    TobaccoListView, BrandsListView, InventoryListView, WishListView,
    brands_add, brands_update,
    tobacco_add, tobacco_update,
    inventory_add, inventory_update,
    wishlist_add, wishlist_update,
    BrandsHomeView, TobaccoHomeView, InventoryHomeView, WishlistHomeView,
    TBCTestView)

urlpatterns = [
    path('', TobaccoOverviewView.as_view(), name='tobacco-home'),
    path('brands/', BrandsHomeView.as_view(), name='tobacco-brands-home'),
    path('tobacco/', TobaccoHomeView.as_view(), name='tobacco-list-home'),
    path('inventory/', InventoryHomeView.as_view(), name='tobacco-inventory-home'),
    path('wishlist/', WishlistHomeView.as_view(), name='tobacco-wishlist-home'),


    path('brands/view/', BrandsListView.as_view(), name='tobacco-brands-view'), # brands_view.html
    path('brands/new/', brands_add, name='tobacco-brands-add'), # brands_form.html
    path('brands/<int:pk>/update/', brands_update, name='tobacco-brands-update'),   # brands_form.html

    path('tobacco/view/', TobaccoListView.as_view(), name='tobacco-list-view'), # tobaccolist_view.html
    path('tobacco/new/', tobacco_add, name='tobacco-list-add'), # tobaccolist_form.html
    path('tobacco/<int:pk>/update/', tobacco_update, name='tobacco-update'), # tobaccolist_form.html
    path('tobacco/<int:pk>/', TobaccoListDetailView.as_view(), name='tobacco-detail'),  # tobaccolist_detail.html

    path('inventory/view/', InventoryListView.as_view(), name='tobacco-inventory-view'),
    path('inventory/add/', inventory_add, name='tobacco-inventory-add'),
    path('inventory/<int:pk>/update/', inventory_update, name='tobacco-inventory-update'),

    path('wishlist/view/', WishListView.as_view(), name='tobacco-wishlist-view'),
    path('wishlist/add/', wishlist_add, name='tobacco-wishlist-add'),
    path('wishlist/<int:pk>/update/', wishlist_update, name='tobacco-wishlist-update'),



]
