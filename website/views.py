# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAuthenticated,
)

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
        return Event.objects.filter(end_date__lt=timezone.now())


class PastEventsList(generics.ListAPIView):
    serializer_class = PastEventSerializer

    def get_queryset(self):
        return Event.objects.filter(end_date__gte=timezone.now())


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
    # permission_classes = [IsAuthenticated]


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

class AlumniCardRegisterView(generics.CreateAPIView):
    queryset = AlumniCard.objects.all()
    serializer_class = AlumniCardSerializer


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
    if active == None:
        # try if a page
        return redirect('/')
    context = {
        'mTabs': mTabs,
        'active': active,
        'base': base,
    }
    return render(request, 'website/page.html', context)
