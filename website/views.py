# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.core.serializers import serialize

from website.serializers import *


class MemberList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class NewsLetterList(generics.ListAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer


class NewsLetterDetailView(generics.RetrieveAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterDetailSerializer


class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()

    serializer_class = EventDetailSerializer


class UpcomingEventsList(generics.ListAPIView):
    serializer_class = UpcomingEventSerializer

    def get_queryset(self):
        """
        This View should return all the upcoming events
        """
        return Event.objects.filter(date__gte=timezone.now())


class PastEventsList(generics.ListAPIView):
    serializer_class = PastEventSerializer

    def get_queryset(self):
        return Event.objects.filter(date__lt=timezone.now())


class MoUListView(generics.ListAPIView):
    queryset = Mou.objects.all()
    serializer_class = MoUSerializer


class MouDetailView(generics.RetrieveAPIView):
    queryset = Mou.objects.all()
    serializer_class = MouDetailSerializer


class HeadlinesListView(generics.ListAPIView):
    queryset = Headline.objects.all()
    serializer_class = HeadlinesSerializer


class HeadlinesDetailView(generics.RetrieveAPIView):
    queryset = Headline.objects.all()
    serializer_class = HeadlinesDetailSerializer


class ShareYourStoryView(generics.ListAPIView):
    queryset = ShareYourStory.objects.all()
    serializer_class = ShareYourStorySerializer


class ShareYourStoryCreateView(generics.CreateAPIView):
    queryset = ShareYourStory.objects.all()
    serializer_class = ShareYourStoryCreateSerializer
    permission_classes = [IsAuthenticated]
