from django.shortcuts import render
from django.shortcuts import render
import random

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .serializers import UserRegisterSerializer
import uuid
from django.core import serializers as core_serializers
class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            
            
            return Response(
                
                
                 status=status.HTTP_201_CREATED
                )
        
        return Response( status=status.HTTP_400_BAD_REQUEST)
