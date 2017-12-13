from rest_framework import serializers
from website.models import Team, Member, NewsLetter, Event


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


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'title', 'link', 'image')
