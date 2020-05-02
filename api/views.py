from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BrandSerializer, TaskSerializer
from tobacco.models import Brands, Task
from django.http import JsonResponse

api_urls = {
    'List': '/brands-list/',
    'Detail View': '/brands-detail/<str:pk>/',
    'Create': '/brands-create/',
    'Update': '/brands-update/<str:pk>/',
    'Delete': '/brands-delete/<str:pk>/',
    'TobaccosByBrands': 'brands-count',
    'WishlistByBrands': 'wish-brands-count',
    'InventoryByBrands': 'inv-brands-count',
    'WishlistByTobacco': 'wish-tbc-count',
    'InventoryByTobacco': 'inv-tbc-count',

}


@api_view(['GET'])
def apiOverview(request):
    return Response(api_urls)


@api_view(['GET'])
def brandsList(request):
    brands = Brands.objects.all().order_by('Brand')
    serializer = BrandSerializer(brands, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def brandsDetail(request, pk):
    brands = Brands.objects.get(pk=pk)
    serializer = BrandSerializer(brands, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def brandsCreate(request):
    serializer = BrandSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("Brand Created")
    return Response(serializer.data)


@api_view(['POST'])
def brandsUpdate(request, pk):
    brands = Brands.objects.get(pk=pk)
    serializer = BrandSerializer(instance=brands, data=request.data)

    if serializer.is_valid():
        serializer.save()
        print("Brand Updated")

    return Response(serializer.data)


@api_view(['DELETE'])
def brandsDelete(request, pk):
    brands = Brands.objects.get(pk=pk)
    brands.delete()

    return Response('Item succsesfully delete!')


# --------------------------------------------------------
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item succsesfully delete!')


# --------------------------------------------------------
# def tobaccoPerBrands(request, *args, **kwargs):
#     brands, counts = [], []
#     for p in Brands.objects.raw(
#             'select TL.id, TL.Brand_id, tb.id, tb.Brand, count(TL.Brand_id) Counts from tobacco_tobaccolist TL JOIN tobacco_brands tb on TL.Brand_id = tb.id GROUP BY Brand_id order by count(Brand_id) DESC;'):
#         brands.append(p.Brand)
#         counts.append(p.Counts)
#
#     data = {
#         "brands": brands,
#         "counts": counts
#     }
#     return JsonResponse(data)


class TobaccosByBrands(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        brands, counts = [], []
        for p in Brands.objects.raw(
                'select TL.id, TL.Brand_id, tb.id, tb.Brand, count(TL.Brand_id) Counts from tobacco_tobaccolist TL JOIN tobacco_brands tb on TL.Brand_id = tb.id GROUP BY Brand_id order by count(Brand_id) DESC;'):
            brands.append(p.Brand)
            counts.append(p.Counts)

        data = {
            "labels": brands,  # Brands
            "default": counts  # Counts
        }
        return Response(data)


class WishlistByBrands(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        brands, counts = [], []
        for p in Brands.objects.raw(
                'select TL.id, TL.Brand_id, tb.id, tb.Brand Brand, count(TL.Brand_id) Counts from tobacco_tobaccolist TL JOIN tobacco_brands tb on TL.Brand_id = tb.id where Wish == true GROUP BY Brand_id order by count(Brand_id) DESC;'):
            brands.append(p.Brand)
            counts.append(p.Counts)

        data = {
            "labels": brands,  # Brands
            "default": counts  # Counts
        }
        return Response(data)


class InventoryByBrands(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        brands, counts = [], []
        for p in Brands.objects.raw(
                'select TL.id, TL.Brand_id, tb.id, tb.Brand Brand, count(TL.Brand_id) Counts from tobacco_tobaccolist TL JOIN tobacco_brands tb on TL.Brand_id = tb.id where Inventory == true GROUP BY Brand_id order by count(Brand_id) DESC;'):
            brands.append(p.Brand)
            counts.append(p.Counts)

        data = {
            "labels": brands,  # Brands
            "default": counts  # Counts
        }
        return Response(data)


class WishlistByTobacco(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        brands, counts = [], []
        for p in Brands.objects.raw(
                'select TL.id, count(TL.Inventory) Counts from tobacco_tobaccolist TL where Wish == true;'):
            brands.append(p.Brand)
            counts.append(p.Counts)

        data = {
            "labels": 'Wishlist',  # Brands
            "default": counts  # Counts
        }
        return Response(data)


class InventoryByTobacco(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        brands, counts = [], []
        for p in Brands.objects.raw(
                'select TL.id, count(TL.Inventory) Counts from tobacco_tobaccolist TL where Inventory == true;'):
            brands.append(p.Brand)
            counts.append(p.Counts)

        data = {
            "labels": 'Inventory',  # Brands
            "default": counts  # Counts
        }
        return Response(data)