from rest_framework import serializers
from django.utils import timezone

from website.models import *


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name', 'role', 'contact_no', 'link', 'team')


class NewsLetterSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = NewsLetter
        fields = ('id', 'title', 'pub_date', 'image')


class NewsLetterDetailSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = NewsLetter
        fields = ('id', 'title', 'content', 'external_link', 'pub_date', 'image')


class ImageSerializer(serializers.ModelSerializer):
    pic = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = EventImage
        fields = ('id', 'pic', 'description')


# class UpcomingEventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         fields = ('id', 'title', 'start_date', 'venue')


# class PastEventSerializer(serializers.ModelSerializer):
#     coverImage = serializers.ImageField(max_length=None, use_url=True)

#     class Meta:
#         model = Event
#         fields = ('id', 'title', 'end_date', 'venue', 'coverImage')


class EventDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'content', 'images','start_date', 'end_date', 'venue', 'link')


class MoUSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mou
        fields = ('id', 'name', 'country')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course', 'duration')


class MouDetailSerializer(serializers.ModelSerializer):
    letter = serializers.FileField(max_length=None, use_url=True)
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Mou
        fields = ('id', 'name', 'country', 'courses', 'letter')


# class PublicationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Publication
#         fields = ('id', 'title', 'type')
#
#
# class PublicationDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Publication
#         fields = ('id', 'type', 'title', 'content')


class HeadlinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = ('id', 'image', 'title')


class HeadlinesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = ('id', 'title', 'image', 'content', 'link')


class ShareYourStoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareYourStory
        fields = ('title', 'description', 'link')


class ShareYourStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareYourStory
        fields = ('id', 'title', 'description', 'link')


class NodeSerializer(serializers.ModelSerializer):
    # children = serializers.SerializerMethodField()

    class Meta:
        model = Node
        fields = '__all__'

class AlumniCardSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(max_length=None, use_url=True)
    photo_sign = serializers.ImageField(max_length=None, use_url=True)
    photo_degree = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = AlumniCard
        fields = '__all__'


class CustomEventSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        resdata = []
        # TODO: Remove Hardcoded stuff
        data1 = data.filter(type='Golden', start_date__gte=timezone.now())
        data2 = data.filter(type='Golden', end_date__lte=timezone.now())
        data3 = data.filter(type='Silver', start_date__gte=timezone.now())
        data4 = data.filter(type='Silver', end_date__lte=timezone.now())
        # data3 = data.filter(type='Golden')
        # data4 = data.filter(type='Golden')
        resdata.append({'Golden': {
            'upcoming': super(CustomEventSerializer, self).to_representation(data1),
            'past': super(CustomEventSerializer, self).to_representation(data2)
            }})
        resdata.append({'Silver': {
            'upcoming': super(CustomEventSerializer, self).to_representation(data3),
            'past': super(CustomEventSerializer, self).to_representation(data4)
            }})
        return resdata

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        list_serializer_class = CustomEventSerializer