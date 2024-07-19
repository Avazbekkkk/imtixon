from rest_framework import serializers
from rest_framework.response import Response

from .models import Food, Category




class PoetSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Food
        fields = '__all__'


class CatSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Category
        fields = '__all__'
