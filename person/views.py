from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Food, Category
from .permissions import IsAdminUserOrReadOnly, IsOwnerUserOrReadOnly
from .serializers import PoetSerializers, CatSerializers



class ListCreatePoet(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = PoetSerializers
    permission_classes = [IsAuthenticated]

class UpdatePoet(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = PoetSerializers
    permission_classes = (IsOwnerUserOrReadOnly, )


class DeleteRetrivePoet(generics.RetrieveDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = PoetSerializers
    permission_classes = (IsAdminUser,)




class ListCreateCatPoet(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializers
    permission_classes = [IsAuthenticated]

class UpdateCatPoet(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializers
    permission_classes = (IsOwnerUserOrReadOnly, )


class DeleteRetriveCatPoet(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializers
    permission_classes = (IsAdminUser,)