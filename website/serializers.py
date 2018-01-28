from rest_framework import serializers

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


class UpcomingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'date', 'venue')


class PastEventSerializer(serializers.ModelSerializer):
    coverImage = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'date', 'venue', 'coverImage')


class EventDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'content', 'images', 'date', 'venue', 'link')


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
    children = serializers.SerializerMethodField()

    class Meta:
        model = Node
        fields = ('url_name', 'title', 'parent', 'visibility', 'external_url', 'level', 'content')

