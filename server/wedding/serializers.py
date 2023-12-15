from rest_framework import serializers
from .models import Wedding, WeddingStatus
from users.serializers import UserSerializer, ProfileSerializer


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingStatus
        fields = ('status_name', )


class WeddingSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    profile = ProfileSerializer(many=False, read_only=True)
    status = StatusSerializer(many=False, read_only=True)

    class Meta:
        model = Wedding
        fields = ('id', 'user', 'profile', 'change_last_name', 'event_datetime', 'status')
