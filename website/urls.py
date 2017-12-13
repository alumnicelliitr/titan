from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^members/$', views.MemberList.as_view(), name='members'),
    url(r'^newsletter/all$', views.NewsLetterList.as_view(), name='newsletter-list'),
    url(r'^newsletter/(?P<pk>[0-9]+)/$', views.NewsLetterDetailView.as_view(), name='newsletter-detail'),
    url(r'^event/all$', views.EventList.as_view(), name='events-list'),
    # events api
    # url(r'^event/(?P<pk>[0-9]+)/$', views.NewsDetailView.as_view(), name='news-detail'),
    # url(r'event/upcoming')
]
