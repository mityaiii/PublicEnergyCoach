from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers
from .Utils import Utils



class AllBlogAPIView(APIView):
    def get(self, request):
        blogs = Utils.get_all('Blog', 'Blog')
        return Response({"data": serializers.BlogSerializer(blogs, many=True).data})


class BlogsByCategoryAPIView(APIView):
    def get(self, request, category):
        blogs = Utils.get_all_by_category('Blog', 'Blog', category)
        return Response({"data": serializers.BlogSerializer(blogs, many=True).data})


class BlogAPIView(APIView):
    def get(self, request, key):
        obj: models.Blog = models.Blog.objects.get(id=key)
        return Response({"data": serializers.BlogSerializer(obj).data})
