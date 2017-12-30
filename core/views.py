# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from core.serializers import *

class Register(APIView):

    serializer_class = RegisterValidationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        tempuser = serializer.save()
        return Response(request.data, status=status.HTTP_202_ACCEPTED)



class Login(APIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        login(request, user)
        user_data = UserSerializer(user).data

        return Response(user_data, status=status.HTTP_202_ACCEPTED)

class Logout(APIView):

    def post(request):
        logout(request)
        return Response({'detail': "user logged out"}, status=status.HTTP_200_OK)


class RegisterUser(APIView):

    permissions_class = [IsAdminUser]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data["password"])
        user.save()
        return Response(request.data, status=status.HTTP_202_ACCEPTED)
