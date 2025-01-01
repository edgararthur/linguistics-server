from django.shortcuts import render

from rest_framework import generics
from .models import News, Collaborations, Consultants, Members, Leadership, Events
from .serializers import ConsultantsSerializer, LeadershipSerializer, MembersSerializer, NewsSerializer, CollaborationsSerializer, EventsSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CollaborationsList(generics.ListCreateAPIView):
    queryset = Collaborations.objects.all()
    serializer_class = CollaborationsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        

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

class HomeView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all().order_by('-date')[:5]

    
class AboutView(generics.ListAPIView):
        queryset = News.objects.all()
        serializer_class = NewsSerializer

        def get_queryset(self):
            return News.objects.all().order_by('-date')[:5]


class EventsList(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class EventsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer