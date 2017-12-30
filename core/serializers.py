from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from core.models import TempUser, User, Alum

class RegisterValidationSerializer(serializers.ModelSerializer):

    class Meta:
        model = TempUser
        fields = ('name', 'email', 'enr_no', 'batch', 'degree_photo')
        extra_kwargs = {
            'enr_no': {'write_only': True},
            'email': {'write_only': True},
            'batch': {'write_only': True},
            'degree_photo': {'write_only': True}
        }


class LoginSerializer(serializers.Serializer):
    enr = serializers.IntegerField(label="Enrollment Number")
    password = serializers.CharField(label="Password")

    def validate(self, attrs):
        enr = attrs.get('enr')
        password = attrs.get('password')

        user = authenticate(enr_no=enr, password=password)
        print(user)
        if not user:
            raise AuthenticationFailed

        attrs['user'] = user
        return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'enr_no', 'image', 'dob', 'batch', 'branch', 'interest', 'campus_groups', 'password')
