from rest_framework import serializers
from .models import News, Collaborations, Members, Consultants, Leadership, Publications, Achievements, Events

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CollaborationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborations
        fields = '__all__'


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'


class ConsultantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultants
        fields = '__all__'


class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = '__all__'


class PublicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = ['id', 'title', 'author', 'year', 'journal', 'volume', 'issue', 'pages', 'abstract', 'url']


class PublicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications 
        fields = '__all__'


class CollaborationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborations
        fields = ['id', 'title', 'year', 'type', 'url']


class CollaborationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborations
        fields = '__all__'


class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['id', 'name', 'position', 'email', 'phone', 'url']


class MemberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = '__all__'

