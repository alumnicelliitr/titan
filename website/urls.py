from django.conf.urls import url

from website.views import *

urlpatterns = [
    # get team members
    # newsletter api
    url(r'^newsletter/all$', NewsLetterList.as_view(), name='newsletter-list'),
    url(r'^newsletter/(?P<pk>[0-9]+)/$', NewsLetterDetailView.as_view(), name='newsletter-detail'),

    # events api
    url(r'^event/(?P<pk>[0-9]+)/$', EventDetailView.as_view(), name='event-detail'),
    url(r'^events/$', EventsList.as_view(), name='events'),

    #   MoUs
    url(r'^mou/$', MoUListView.as_view(), name='mous-list'),
    url(r'^mou/(?P<pk>[0-9]+)/$', MouDetailView.as_view(), name='mou-detail'),

    # Headlines
    url(r'^headlines/$', HeadlinesListView.as_view(), name='headlines'),
    # url(r'^headlines/trending$', HeadlinesTrendingListView.as_view(), name='headlines'),
    url(r'^headline/(?P<pk>[0-9]+)/$', HeadlinesDetailView.as_view(), name='headlines-detail'),

    # Share Your Story
    url(r'^shareYourStory/$', ShareYourStoryView.as_view(), name='share-your-stories'),
    # Alumni can register for Share You Story
    url(r'^shareYourStory/create$', ShareYourStoryCreateView.as_view(), name='share-your-stories-create'),
    # Know Your Alumni
    url(r'^knowYourAlum/$', KnowYourAlumniView.as_view(), name='know-your-alums'),
    # Alumni can register for Share You Story
    url(r'^knowYourAlum/create$', KnowYourAlumniCreateView.as_view(), name='know-your-alums-create'),
    # Nodes API for Header
    url(r'^nodes/$', NodeViews.as_view(), name='send-nodes'),
    # Alumni Card Register API
    url(r'^alumni_card/register$', AlumniCardRegisterView.as_view(), name='alumni-card-register'),
    # Awards API
    url(r'^awards/$', AwardsListView.as_view(), name='awards' ),
    # Donations API
    url(r'^donation_schemes/$', DonationSchemeListView.as_view(), name='awards' )
]
