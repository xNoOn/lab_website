from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BrandSerializer, TaskSerializer
from tobacco.models import Brands, Task


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def brandsList(request):
    brands = Brands.objects.all().order_by('BrandID')
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
@api_view(['GET'])
def brandsCount(request): #Anzahl Brands in der TobaccoList
    brands = Brands.objects.raw('select TL.Brand_id, TL.Name, TL.id from tobacco_tobaccolist TL GROUP BY Brand_id;')
    print(brands.columns)
    serializer = BrandSerializer(brands, many=True)
    return Response(serializer.data)
