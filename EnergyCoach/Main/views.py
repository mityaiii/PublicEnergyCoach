from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


class ContactFormAPIView(APIView):
    def get(self, request):
        contacts = models.ContactForm.objects.all()
        return Response({'data': serializers.ContactFormSerializer(contacts, many=True).data})

    def post(self, request):
        contact = serializers.ContactFormSerializer(data=request.data)
        if contact.is_valid():
            contact.save()
            return Response({'data': contact.data})
        else:
            return Response({'status': '404', 'data': contact.data})


class MetaAPIView(APIView):
    def get(self, request, key):
        obj: models.Meta = models.Meta.objects.get(key=key)
        return Response({"data": serializers.MetaSerializer(obj).data})
