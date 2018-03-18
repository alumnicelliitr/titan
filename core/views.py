# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, logout
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from datetime import datetime
import requests as http_requests
from django.core.mail import EmailMultiAlternatives, get_connection
import urllib, ssl
import os
import json
from django.core.files import File
from titan import settings
from core.serializers import *


class Register(APIView):
    pass
    """
    serializer_class = RegisterValidationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        tempuser = serializer.save()
        return Response(request.data, status=status.HTTP_202_ACCEPTED)
    """


class Login(APIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        login(request, user)
        user_data = UserSerializer(user).data

        return Response(user_data, status=status.HTTP_202_ACCEPTED)

class LoggedInUser(APIView):
    def get(self, request):
        if request.user.is_authenticated():
            user_data = UserSerializer(request.user).data
            return Response(user_data, status=status.HTTP_202_ACCEPTED)

        return Response('logged_out', status=status.HTTP_401_UNAUTHORIZED)

class Logout(APIView):

    def post(request):
        logout(request)
        return Response({'detail': "user logged out"}, status=status.HTTP_200_OK)


class RegisterUser(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer      


class OAuthRedirectView(APIView):
    permission_classes = []

    @staticmethod
    def get(request):
        auth_code = request.GET.get('code')
        print(auth_code)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        payload1 = "client_id=%s&" \
                   "client_secret=%s&" \
                   "code=%s" % (os.environ.get('CLIENT_ID'), os.environ.get('CLIENT_SECRET'), auth_code)
        req1 = http_requests.post('https://channeli.in/oauth/gettoken/',
                                  data=payload1,
                                  headers=headers)
        print(req1)
        if not req1.status_code == 200:
            return Response(status=status.HTTP_403_FORBIDDEN)

        access_token = json.loads(req1.text)['access_token']
        payload2 = "client_id=%s&" \
                   "client_secret=%s&" \
                   "access_token=%s" % (os.environ.get('CLIENT_ID'), os.environ.get('CLIENT_SECRET'), access_token)
        req2 = http_requests.post('https://channeli.in/oauth/getuserdata/',
                                  data=payload2,
                                  headers=headers)
        print(req2.status_code)
        if not req2.status_code == 200:
            return Response(status=status.HTTP_403_FORBIDDEN)

        oauth_user_data = json.loads(req2.text)
        oauth_user_data['username'] = int(oauth_user_data['username'])
        user, created = User.objects.get_or_create(enr_no=oauth_user_data['username'])
        if created:
            user.name = oauth_user_data['name']

            if oauth_user_data['date_of_birth']:
                user.dob = datetime.strptime(str(oauth_user_data['date_of_birth']), '%Y-%m-%d').date()
            if oauth_user_data['admission_year']:

                user.joining_date = datetime.strptime(str(oauth_user_data['admission_year'])+'-07-15', '%Y-%m-%d').date()
            if oauth_user_data['passout_year']: 

                user.leaving_date = datetime.strptime(str(oauth_user_data['passout_year'])+'-05-15', '%Y-%m-%d').date()
            
            user.gender = oauth_user_data['gender']
            user.email_1 = oauth_user_data['email']
            user.save()

            if oauth_user_data['photo']:
                img_url = 'http://people.iitr.ernet.in/media/'+oauth_user_data['photo']
                name = oauth_user_data['photo'].split('/')[-1]
                result = urllib.urlretrieve(img_url)
                print(result)
                user.image.save(name, File(open(result[0])), save=True)

            if oauth_user_data['is_alumni']:
                Alumni.objects.create(user = user, is_verified=True)   

        # https://channeli.in:8080/media/
        # 5ce1f230e41e6c95ff76b4844bc68d7af264c711
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        user_data = UserSerializer(user).data
        return Response(user_data, status=status.HTTP_202_ACCEPTED)


from django.contrib.sites.shortcuts import get_current_site
from django import forms
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

class UserForm(forms.Form):
    email = forms.EmailField()  
    password = forms.CharField(widget=forms.PasswordInput())    

def unsubscribe(request,key):
    message = ''
    try:
        subscriber = Subscriber.objects.get(subscription_key=key)
        subscriber.is_subscribed = False
        mail_subject = 'Unsubscribe to AlumniIITR'
        current_site = get_current_site(request)
        text = render_to_string('core/unsubscribe.html', {
                'domain':current_site.domain,
                'sub': subscriber,
            })
        to_email = subscriber.user.email_1
        if to_email:
            my_username = settings.EMAIL_HOST_USER
            connection = get_connection() # uses SMTP server specified in settings.py
            connection.open()
            email = EmailMultiAlternatives(mail_subject, text, my_username, to=[to_email])
            email.content_subtype = 'html'
            email.send()
            connection.close() 
        subscriber.save()
        message = 'Unsubscribed successfully'
    except:
        message = 'Invalid Subscription key'
    return render(request, 'core/sub-unsub.html', {'message':message, }) 

def resubscribe(request,key):
    message = ''
    try:
        subscriber = Subscriber.objects.get(subscription_key=key)
        subscriber.is_subscribed = True
        subscriber.save()
        mail_subject = 'Resubscribe to AlumniIITR'
        current_site = get_current_site(request)
        text = render_to_string('core/resubscribe.html', {
                'domain':current_site.domain,
                'sub': subscriber,
            })
        to_email = subscriber.user.email_1
        if to_email:
            my_username = settings.EMAIL_HOST_USER
            connection = get_connection() # uses SMTP server specified in settings.py
            connection.open()
            email = EmailMultiAlternatives(mail_subject, text, my_username, to=[to_email])
            print('done done')
            email.content_subtype = 'html'
            email.send()
            connection.close() 
        subscriber.save()
        message = 'Subscribed successfully'
    except:
        message = 'Invalid Subscription key'
    return render(request, 'core/sub-unsub.html', {'message':message, })  


def send_mail(request,id):
    message = get_object_or_404(EmailMessage, pk=id)
    subscribers = Subscriber.objects.filter(is_subscribed=True)
    mail_subject = message.subject
    current_site = get_current_site(request)
    form = UserForm()
    success=False
    if request.method == "POST":
        form = UserForm(request.POST)
    if form.is_valid():
        my_username = form.cleaned_data['email']
        my_password = form.cleaned_data['password']
        connection = get_connection( 
                            username=my_username, 
                            password=my_password,
                            fail_silently=False)
        connection.open()
        emails = []
        for sub in subscribers:
            text = render_to_string('core/msg.html', {
                'domain':current_site.domain,
                'sub': sub,
                'msg': message,
            })
            to_email = sub.user.email_1
            #email = EmailMsg(mail_subject, text, to=[to_email], connection=connection)
            if to_email:
                print(to_email)
                email = EmailMultiAlternatives(mail_subject, text, my_username, [to_email])
                #email.attach_alternative(text_content, "text/html")
                email.content_subtype = 'html'
                emails.append(email)
                #email.send()
        connection.send_messages(emails) 
        connection.close()
        success = True
    context = {
            'userform'  : form,
            'success' : success,
        }
    return render(request, 'core/mailform.html', context) 

