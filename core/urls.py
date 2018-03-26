from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/user/$', views.RegisterUser.as_view(), name='register.user'),
    url(r'^login/user/$',  views.LoggedInUser.as_view(), name='register'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^user/detail/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name = 'userdetail'),
    url(r'^login/$', views.OAuthRedirectView.as_view(), name = 'oauth'),
    url(r'^unsubscribe/(?P<key>(.*))/$',views.unsubscribe, name='unsubscribe'),
    url(r'^resubscribe/(?P<key>(.*))/$',views.resubscribe, name='resubscribe'),
    url(r'^send/(?P<id>[0-9]+)/$', views.send_mail, name='sendmsg'),
    url(r'^team/$', views.MemberList.as_view(), name = 'userdetail'),
    url(r'^visitor/unsubscribe/(?P<key>(.*))/$', views.unsubscribe_visitor, name = 'unsubscribe_visitor'),
    url(r'^user/contact/$',  views.ContactCreate.as_view(), name='create-contact'),
    url(r'^user/contact/(?P<key>(.*))/$', views.ContactDetail.as_view(), name = 'update-contact'),
    url(r'^user/social/$',  views.SocialCreate.as_view(), name='create-social'),
    url(r'^user/social/(?P<key>(.*))/$', views.SocialDetail.as_view(), name = 'update-social'),
    url(r'^user/userlocation/$',  views.UserLocationCreate.as_view(), name='create-userlocation'),
    url(r'^user/userlocation/(?P<key>(.*))/$', views.UserLocationDetail.as_view(), name = 'update-userlocation'),
    url(r'^user/experience/$',  views.ExperienceCreate.as_view(), name='create-experience'),
    url(r'^user/experience/(?P<key>(.*))/$', views.ExperienceDetail.as_view(), name = 'update-experience'),
    url(r'^user/skill/(?P<key>(.*))/$', views.SkillCreate.as_view(), name = 'create-skill'),
    url(r'^nominate/$', views.Nominate.as_view(), name='nominate'),
]
