# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from website.models import Member, NewsLetter, Event
from website.serializers import MemberSerializer, NewsLetterSerializer, NewsLetterDetailSerializer, EventSerializer


class MemberList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class NewsLetterList(generics.ListAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer


class NewsLetterDetailView(generics.RetrieveAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterDetailSerializer


class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer





