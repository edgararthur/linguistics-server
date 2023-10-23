from rest_framework import serializers
from .models import News, Collaborations, Members, Consultants, Leadership

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