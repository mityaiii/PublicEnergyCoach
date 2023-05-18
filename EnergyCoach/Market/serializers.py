from rest_framework import serializers
from .models import MarketProduct

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketProduct
        fields = '__all__'
