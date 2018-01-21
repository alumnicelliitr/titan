from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$',  views.Register.as_view(), name='register'),
    url(r'^register/user/$', views.RegisterUser.as_view(), name='register.user'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
]