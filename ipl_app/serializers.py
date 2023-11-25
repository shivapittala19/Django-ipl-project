from rest_framework import serializers
from .models import Matches, Deliveries

class MatchesSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Matches
        fields = "__all__"
        
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliveries
        fields = '__all__'  