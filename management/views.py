from django.shortcuts import render

from rest_framework import generics
from .models import News, Collaborations, Consultants, Members, Leadership
from .serializers import ConsultantsSerializer, LeadershipSerializer, MembersSerializer, NewsSerializer, CollaborationsSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CollaborationsList(generics.ListCreateAPIView):
    queryset = Collaborations.objects.all()
    serializer_class = CollaborationsSerializer


class CollaborationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collaborations.objects.all()
    serializer_class = CollaborationsSerializer


class ConsultantsList(generics.ListCreateAPIView):
    queryset = Consultants.objects.all()
    serializer_class = ConsultantsSerializer


class ConsultantsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultants.objects.all()
    serializer_class = ConsultantsSerializer


class MembersList(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer


class MembersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer


class LeadershipList(generics.ListCreateAPIView):
    queryset = Leadership.objects.all()
    serializer_class = LeadershipSerializer


class LeadershipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leadership.objects.all()
    serializer_class = LeadershipSerializer
