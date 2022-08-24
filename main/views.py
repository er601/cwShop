from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from main.serializers import ProductSerializer, ProductDetailSerializer
from main.models import Product


@api_view(['GET'])
def product_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_item_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product not exist found'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ProductDetailSerializer(product)
    return Response(data=serializer.data)


@api_view(['GET'])
def test_view(request):
    dict_ = {
        'text': 'Hello world!!!',
        'int': 100,
        'float': 9.99,
        'boolean': True,
        'list': [
            1, 2, 3
        ],
        'dict': {
            'new': 'yes'
        },
    }
    return Response(data=dict_)
