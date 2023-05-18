from rest_framework import serializers
from . import models


class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactForm
        fields = '__all__'


class ContactFormSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return models.ContactForm.objects.create(**validated_data)

    class Meta:
        model = models.ContactForm
        fields = '__all__'
