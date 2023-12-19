from rest_framework import serializers
from . import models


class AbstractUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AbstractProfile
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RelativeStatus
        fields = ('status_name', )


class RelativeSerializer(serializers.ModelSerializer):
    abstract_profile = AbstractUserSerializer(many=False, read_only=True)
    status = StatusSerializer(many=False, read_only=True)
    class Meta:
        model = models.Relatives
        fields = ('id', 'abstract_profile', 'status')