from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers, models
from .Utils import Utils


class AllProductAPIView(APIView):
    def get(self, request):
        products = Utils.get_all('Product', 'Product')
        return Response({"data": serializers.ProductSerializer(products, many=True).data})


class ProductsByCategoryAPIView(APIView):
    def get(self, request, category):
        products = Utils.get_all_by_category('Product', 'Product', category)
        return Response({"data": serializers.ProductSerializer(products, many=True).data})


class ProductAPIView(APIView):
    def get(self, request, key):
        obj: models.Product = models.Product.objects.get(id=key)
        return Response({"data": serializers.ProductSerializer(obj).data})
