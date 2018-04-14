from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from core.models import *

"""
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

"""
class LoginSerializer(serializers.Serializer):
    enr = serializers.IntegerField(label="Enrollment Number")
    password = serializers.CharField(label="Password")

    def validate(self, attrs):
        enr = attrs.get('enr')
        password = attrs.get('password')

        user = authenticate(enr_no=enr, password=password)

        if not user:
            raise AuthenticationFailed
        attrs['user'] = user
        return attrs

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    branch = serializers.CharField(source='get_branch_display')
    class Meta:
        model = User
        fields = ('name', 'email', 'enr_no', 'course', 'branch', 'password')

    def create(self, validated_data, instance=None):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = '__all__'
        read_only_fields = ('id', 'user',)


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ('id', 'user',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('id', 'user',)


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'
        read_only_fields = ('id', 'user',)


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('id',)


class UserLocationSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = UserLocation
        fields = '__all__'
        read_only_fields = ('id', 'user',)


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'
        read_only_fields = ('id',)


class ExperienceSerializer(serializers.ModelSerializer):
    org = OrganisationSerializer()
    class Meta:
        model = Experience
        fields = '__all__'
        read_only_fields = ('id', 'user',)


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        read_only_fields = ('id','user')


class GetUserSerializer(serializers.ModelSerializer):
    alum = AlumniSerializer()
    team = TeamSerializer()
    contacts = ContactSerializer(many=True)
    socials = SocialSerializer(many=True)
    locations = UserLocationSerializer(many=True)
    experiences = ExperienceSerializer(many=True)
    skills = SkillSerializer(many=True)
    class Meta:
        model = User
        fields = ('name', 'email', 'email_1', 'enr_no', 'course', 'branch',
            'image', 'leaving_date', 'joining_date', 'dob',
            'hostel', 'room_no', 'gender', 'aadhar_no',
            'alum','team', 'contacts', 'socials', 'locations', 'experiences',
            'skills' )

class CustomEventSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        resdata = []
        data1 = data.filter(member_type='F')
        data2 = data.filter(member_type='P')
        data3 = data.filter(member_type='C')
        resdata.append({'Founding': super(CustomEventSerializer, self).to_representation(data1)})
        resdata.append({'Passed': super(CustomEventSerializer, self).to_representation(data2)})
        resdata.append({'Current': super(CustomEventSerializer, self).to_representation(data3)})
        return resdata

class MemberSerializer(serializers.ModelSerializer):
    user = GetUserSerializer(many=False)
    class Meta:
        model = Team
        fields = '__all__'
        list_serializer_class = CustomEventSerializer


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'
        read_only_fields = ('id','is_subscribed', 'subscription_key')


class DistinguishedAlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistinguishedAlumni
        fields = '__all__'
        read_only_fields = ('id',)
