from rest_framework import serializers
from .models import Wedding, WeddingStatus, Witnesses, Children, Child, BirthSertificate, ChildStatus
from users.serializers import UserSerializer, ProfileSerializer
from relationships.serializers import AbstractUserSerializer


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


class WitnessSerializer(serializers.ModelSerializer):
    wedding = WeddingSerializer(many=False, read_only=True)
    witness = AbstractUserSerializer(many=False, read_only=True)

    class Meta:
        model = Witnesses
        fields = ("id", "wedding", "witness",)


class BirthSertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirthSertificate
        fields = "__all__"

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"

class ChildStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildStatus
        fields = "__all__"


class ChildrenSerializer(serializers.ModelSerializer):
    child = ChildSerializer(many=False, read_only=True)
    birth_sertificate = BirthSertificateSerializer(many=False, read_only=True)
    status = ChildStatusSerializer(many=False, read_only=True)

    class Meta:
        model = Children
        fields = "__all__"