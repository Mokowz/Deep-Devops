from rest_framework.serializers import ModelSerializer
from .models import Food

class FoodSerializer(ModelSerializer):
  class Meta:
    model = Food
    fields = ['id', 'name', 'country_origin']