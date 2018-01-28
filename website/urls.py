from django.conf.urls import url

from website.views import *

urlpatterns = [
    # get team members
    url(r'^members/$', MemberList.as_view(), name='members'),

    # newsletter api
    url(r'^newsletter/all$', NewsLetterList.as_view(), name='newsletter-list'),
    url(r'^newsletter/(?P<pk>[0-9]+)/$', NewsLetterDetailView.as_view(), name='newsletter-detail'),

    # events api
    url(r'^event/(?P<pk>[0-9]+)/$', EventDetailView.as_view(), name='event-detail'),
    url(r'^event/upcoming/$', UpcomingEventsList.as_view(), name='upcoming-events'),
    url(r'^event/past/$', PastEventsList.as_view(), name='past-events'),

    #   MoUs
    url(r'^mou/$', MoUListView.as_view(), name='mous-list'),
    url(r'^mou/(?P<pk>[0-9]+)/$', MouDetailView.as_view(), name='mou-detail'),

    # Headlines
    url(r'^headlines/$', HeadlinesListView.as_view(), name='headlines'),
    url(r'^headline/(?P<pk>[0-9]+)/$', HeadlinesDetailView.as_view(), name='headlines-detail'),

    # Share Your Story
    url(r'^shareYourStory/$', ShareYourStoryView.as_view(), name='know-your-stories'),
    # ALumni can register for Share You Story
    url(r'^shareYourStory/create$', ShareYourStoryCreateView.as_view(), name='know-your-stories-create'),

    # Added pages
    url(r'^test$', IndexView.as_view()),
    url(r'^test1$', index),
    url(r'^(?P<level0>[a-z]+)/(?P<level1>[a-z]+)$', level),
]
