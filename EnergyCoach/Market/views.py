from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers, models
from .Utils import Utils


class AllMarketProductAPIView(APIView):
    def get(self, request):
        products = Utils.get_all('Market', 'MarketProduct')
        return Response({"data": serializers.MarketProductSerializer(products, many=True).data})


class MarketProductsByCategoryAPIView(APIView):
    def get(self, request, category):
        products = Utils.get_all_by_category('Market', 'MarketProduct', category)
        return Response({"data": serializers.MarketProductSerializer(products, many=True).data})


class MarketProductAPIView(APIView):
    def get(self, request, key):
        obj: models.MarketProduct = models.MarketProduct.objects.get(id=key)
        return Response({"data": serializers.MarketProductSerializer(obj).data})
