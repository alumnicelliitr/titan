from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/user/$', views.RegisterUser.as_view(), name='register.user'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^login/user/$',  views.LoggedInUser.as_view(), name='register'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^user/detail/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name = 'userdetail')
]
