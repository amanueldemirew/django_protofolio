from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from rest_framework import status
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        query_set = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(query_set, many=True, context={'request':request})
        return Response(serializer.data)
    elif request.method == 'Post':
        serializer = ProductSerializer(data=request.data)
        # serializer.validate.data
        Response("ok")




@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view()  
def collection_detail(request, pk):
    return Response('ok')