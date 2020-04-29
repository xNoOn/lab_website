from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Brands, TobaccoList, Inventory, Wishlist
from django.contrib.auth.decorators import login_required
from .forms import TobaccoForm, BrandsForm, InventoryForm, WishForm
from django.contrib import messages


class TobaccoOverviewView(LoginRequiredMixin, TemplateView):
    template_name = 'tobacco/home.html'

    def get(self, request, **kwargs):
        return self.render_to_response({})


# ---------------------------------------ListView---------------------------------------
class BrandsListView(LoginRequiredMixin, ListView):
    model = Brands
    template_name = 'tobacco/brands_view.html'
    context_object_name = 'brands'
    ordering = ["Brand"]
    paginate_by = 7


class TobaccoListView(LoginRequiredMixin, ListView):
    model = TobaccoList
    template_name = 'tobacco/tobaccolist_view.html'
    context_object_name = 'tobacco'
    ordering = ["-Name"]
    paginate_by = 7


class InventoryListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = 'tobacco/inventory_view.html'
    context_object_name = 'inventory'
    ordering = ["Quantity"]
    #paginate_by = 10


class WishListView(LoginRequiredMixin, ListView):
    model = Wishlist
    template_name = 'tobacco/wishlist_view.html'
    context_object_name = 'wish'
    ordering = ["Priority"]
    #paginate_by = 10


class BrandsHomeView(LoginRequiredMixin, ListView):
    model = Brands
    template_name = 'tobacco/brand_home.html'
    context_object_name = 'brands'
    paginate_by = 8
    ordering = ['Brand']


class TobaccoHomeView(LoginRequiredMixin, ListView):
    model = TobaccoList
    template_name = 'tobacco/tobacco_home.html'
    context_object_name = 'tobacco'
    paginate_by = 8
    ordering = ['Name']


class InventoryHomeView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = 'tobacco/inventory_home.html'
    context_object_name = 'inventory'
    #paginate_by = 8
    ordering = ['-Quantity']


class WishlistHomeView(LoginRequiredMixin, ListView):
    model = Wishlist
    template_name = 'tobacco/wishlist_home.html'
    context_object_name = 'wishlist'
    #paginate_by = 8
    ordering = ['Priority']

# ---------------------------------------CreateView---------------------------------------
# class BrandCreateView(LoginRequiredMixin, CreateView):
#     model = Brands
#     fields = ['Brand', 'Price', 'Weight', 'image']
#     success_url = '/tobacco/brands/view/'

@login_required()
def brands_add(request):
    if request.method == 'POST':
        b_form = BrandsForm(request.POST, request.FILES)
        if b_form.is_valid():
            b_form.save()
            messages.success(request, f'Brands has been created!')
            return redirect('tobacco-brands-view')
    else:
        b_form = BrandsForm()

    context = {
        'b_form': b_form,
    }
    return render(request, 'tobacco/brands_form.html', context)


# class TobaccoCreateView(LoginRequiredMixin, CreateView):
#     model = TobaccoList
#     fields = ['BrandID', 'Name', 'Taste', 'Inventory','Comment', 'Image', 'QTaste', 'QSmoke', 'QCut']
#     success_url = '/tobacco/tobacco/view/'

@login_required()
def tobacco_add(request):
    if request.method == 'POST':
        t_form = TobaccoForm(request.POST, request.FILES)
        if t_form.is_valid():
            t_form.save()
            messages.success(request, f'Tobacco has been created!')
            return redirect('tobacco-list-view')
    else:
        t_form = TobaccoForm()

    context = {
        't_form': t_form
    }
    return render(request, 'tobacco/tobaccolist_form.html', context)


# class InventoryCreateView(LoginRequiredMixin, CreateView):
#     model = Inventory
#     fields = ['TobaccoID', 'Quantity']
#     success_url = '/tobacco/inventory/view'

@login_required()
def inventory_add(request):
    if request.method == 'POST':
        i_form = InventoryForm(request.POST, request.FILES)
        if i_form.is_valid():
            i_form.save()
            messages.success(request, f'Inventory Item has been created!')
            return redirect('tobacco-inventory-view')
    else:
        i_form = InventoryForm()

    context = {'i_form': i_form}
    return render(request, 'tobacco/inventory_form.html', context)


@login_required()
def wishlist_add(request):
    if request.method == 'POST':
        w_form = WishForm(request.POST, request.FILES)
        if w_form.is_valid():
            w_form.save()
            messages.success(request, f'Wishlist Item has been created!')
            return redirect('tobacco-wishlist-view')
    else:
        w_form = WishForm()

    context = {'w_form': w_form}
    return render(request, 'tobacco/wishlist_form.html', context)


# ---------------------------------------DetailView---------------------------------------
class TobaccoListDetailView(LoginRequiredMixin, DetailView):  # tobaccolist_detail.html
    model = TobaccoList


# ---------------------------------------UpdateView---------------------------------------
@login_required()
def brands_update(request, pk):
    template = 'tobacco/brands_form.html'
    brands = get_object_or_404(Brands, pk=pk)
    if request.method == 'POST':
        form = BrandsForm(request.POST or None, request.FILES or None, instance=brands)

        if form.is_valid():
            form.save()
            messages.success(request, f'Brand has been updated!')
            return redirect('tobacco-brands-view')
    else:
        form = BrandsForm(instance=brands)

    context = {'b_form': form}
    return render(request, template, context)


# class TobaccoListUpdateView(LoginRequiredMixin, UpdateView):
#     model = TobaccoList
#     fields = ['TobaccoID', 'BrandID', 'Name', 'Taste', 'Inventory', 'Comment', 'Image', 'QTaste', 'QSmoke', 'QCut']
#     success_url = '/tobacco/tobacco/view/'

@login_required()
def tobacco_update(request, pk):
    template = 'tobacco/tobaccolist_form.html'
    tobacco = get_object_or_404(TobaccoList, pk=pk)
    if request.method == 'POST':
        form = TobaccoForm(request.POST or None, request.FILES or None, instance=tobacco)

        if form.is_valid():
            form.save()
            messages.success(request, f'Tobacco has been updated!')
            return redirect('tobacco-list-view')
    else:
        form = TobaccoForm(instance=tobacco)

    context = {'t_form': form}
    return render(request, template, context)


# class InventoryUpdateView(LoginRequiredMixin, UpdateView):
#     model = Inventory
#     fields = ['TobaccoID', 'Quantity']
#     success_url = '/tobacco/inventory/view'

@login_required()
def inventory_update(request, pk):
    template = 'tobacco/inventory_form.html'
    inventory = get_object_or_404(Inventory, pk=pk)
    form = InventoryForm(request.POST or None, instance=inventory)

    if form.is_valid():
        form.save()
        messages.success(request, f'Inventory has been updated!')
        return redirect('tobacco-inventory-view')

    context = {'i_form': form}
    return render(request, template, context)


@login_required()
def wishlist_update(request, pk):
    template = 'tobacco/wishlist_form.html'
    wish = get_object_or_404(Wishlist, pk=pk)
    form = WishForm(request.POST or None, instance=wish)

    if form.is_valid():
        form.save()
        messages.success(request, f'Wishlist has been updated!')
        return redirect('tobacco-wishlist-view')

    context = {'w_form': form}
    return render(request, template, context)
