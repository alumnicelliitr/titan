# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAuthenticated,
)
from django.shortcuts import get_object_or_404

from website.serializers import *


class NewsLetterList(generics.ListAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer


class NewsLetterDetailView(generics.RetrieveAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterDetailSerializer


class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer


class EventsList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    # def get_queryset(self):
    #     return Event.objects.filter(end_date__gte=timezone.now())


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

    # def perform_create(self, serializer):
    #     print(self.request.user)
    #     if not self.request.user:
    #         return Response({'detail': "Not logged In"}, status=status.HTTP_404_NOT_FOUND)
    #
    #     user = get_object_or_404(User, pk=self.request.user)
    #     serializer.save(user=user.username)


class KnowYourAlumniView(generics.ListAPIView):
    queryset = KnowYourAlumni.objects.all()
    serializer_class = KnowYourAlumniSerializer


class KnowYourAlumniCreateView(generics.CreateAPIView):
    queryset = KnowYourAlumni.objects.all()
    serializer_class = KnowYourAlumniCreateSerializer

    # def perform_create(self, serializer):
    #     print(self.request.user)
    #     user = get_object_or_404(User, pk=self.request.user.id)
    #     serializer.save(user=user.username)


# class HeadlinesTrendingListView(generics.ListAPIView):
#     serializer_class = HeadlinesSerializer
#
#     def get_queryset(self):
#         return Headline.objects.filter(mainPage=False)
#
#
class NodeViews(APIView):
    def get(self, request, format=None):
        nodes = Node.objects.all()
        stuff = load_nodes(0)
        print(stuff)
        s = NodeSerializer(stuff)
        print(s)
        serializer = []
        i = 0
        # x = Node.objects.filter(Q(parent=my_person) | Q(parent__parent=my_person) | Q(parent__parent__parent=my_person))
        for node in nodes:
            serializer_data = NodeSerializer(node.get_all_children(), many=True)
            # if len(serializer_data.data) > 1 and serializer_data.data[0]['level'] == 0:
            serializer.append(serializer_data.data)
        for i in serializer:
            for j in i:
                j['url_name']
        return Response(serializer)


# class NodeViews(generics.CreateAPIView):
#     queryset = Node.objects.all()
#     print(queryset)
#     serializer_class = NodeSerializer

class AwardsListView(generics.ListAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer


class DonationSchemeListView(generics.ListAPIView):
    queryset = DonationScheme.objects.all()
    serializer_class = DonationSchemeSerializer


def load_nodes(level, parent=None):
    mTabs = Node.objects.filter(visibility=True, level=level, parent=parent)
    # serializer = NodeSerializer(mTabs)
    for tab in mTabs:
        if tab.external_url:
            tab.url = tab.external_url
        else:
            try:
                if parent.url:
                    tab.url = parent.url + "/" + tab.url_name
                else:
                    tab.url = "/" + tab.url_name
            except:
                tab.url = "/" + tab.url_name
        tab.children = load_nodes(level + 1, tab)
        print(tab)
    return mTabs


def load_level(url_name, level=0):
    try:
        active = Node.objects.filter(level=level, url_name=url_name).get()
        active.url = "/" + url_name
        active.children = load_nodes(level + 1, active)
        return active
    except:
        return None


def level(request, level0, level1=None, level2=None):
    mTabs = load_nodes(0, None)
    if level1 == None:
        active = load_level(level0, 0)
    elif level2 == None:
        active = load_level(level1, 1)
    else:
        active = load_level(level2, 2)
    base = load_level(level0, 0)


class AlumniCardRegisterView(generics.CreateAPIView):
    serializer_class = AlumniCardSerializaler

    def perform_create(self, serializer):
        # user = get_object_or_404(User, pk=self.request.user.id)

        print(hasattr(self.request.user, 'alumnicard'))
        if hasattr(self.request.user, 'alumnicard'):
            return Response({'detail': "Already registered for alumni card"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
