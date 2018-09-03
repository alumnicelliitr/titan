from rest_framework import serializers
from django.utils import timezone

from website.models import *


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
        fields = ('id', 'title', 'content', 'images', 'start_date', 'end_date', 'venue', 'link')


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
        fields = '__all__'


class ShareYourStorySerializer(serializers.ModelSerializer):
    # user = serializers.RelatedField(source='user', read_only=True)
    class Meta:
        model = ShareYourStory
        fields = '__all__'


class KnowYourAlumniCreateSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = KnowYourAlumni
        fields = ('name', 'branch', 'year', 'thumbnail', 'title', 'description', 'link')


class KnowYourAlumniSerializer(serializers.ModelSerializer):
    # user = serializers.RelatedField(source='user', read_only=True)

    class Meta:
        model = KnowYourAlumni
        fields = '__all__'


class NodeSerializer(serializers.ModelSerializer):
    # children = serializers.SerializerMethodField()

    class Meta:
        model = Node
        fields = '__all__'


class AlumniCardSerializaler(serializers.ModelSerializer):
    photo = serializers.ImageField(max_length=None, use_url=True)
    photo_sign = serializers.ImageField(max_length=None, use_url=True)
    photo_degree = serializers.ImageField(max_length=None, use_url=True)
    delivered= serializers.BooleanField(read_only=True)
    def get_queryset():
        queryset=User.objects.all()
    class Meta:
        model = AlumniCard
        fields = '__all__'

class CurrentBatchAlumniCardSerializaler(serializers.ModelSerializer):
    photo = serializers.ImageField(max_length=None, use_url=True)
    photo_sign = serializers.ImageField(max_length=None, use_url=True)
    photo_degree = serializers.ImageField(max_length=None, use_url=True)
    delivered= serializers.BooleanField(read_only=True)
    def get_queryset():
        queryset=User.objects.all()
    class Meta:
        model = CurrentBatchAlumniCard
        fields = '__all__'


class CustomEventSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        resdata = []
        # TODO: Remove Hardcoded stuff
        data1 = data.filter(type='AM', start_date__gte=timezone.now())
        data2 = data.filter(type='AM', end_date__lte=timezone.now())
        data3 = data.filter(type='GL', start_date__gte=timezone.now())
        data4 = data.filter(type='GL', end_date__lte=timezone.now())
        data5 = data.filter(type='RU', start_date__gte=timezone.now())
        data6 = data.filter(type='RU', end_date__lte=timezone.now())
        # data3 = data.filter(type='Golden')
        # data4 = data.filter(type='Golden')
        data1 = data1 + data5
        data2 = data2 + data6
        resdata.append({'Alumni Meet': {
            'upcoming': super(CustomEventSerializer, self).to_representation(data1),
            'past': super(CustomEventSerializer, self).to_representation(data2)
        }})
        resdata.append({'Guest Lecture': {
            'upcoming': super(CustomEventSerializer, self).to_representation(data3),
            'past': super(CustomEventSerializer, self).to_representation(data4)
        }})
        # resdata.append({'Re Union': {
        #     'upcoming': super(CustomEventSerializer, self).to_representation(data5),
        #     'past': super(CustomEventSerializer, self).to_representation(data6)
        # }})
        return resdata


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        list_serializer_class = CustomEventSerializer


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'


class DonationSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationScheme
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    # user = serializers.RelatedField(source='user', read_only=True)

    class Meta:
        model = News
        fields = '__all__'