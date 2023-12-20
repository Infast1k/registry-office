from rest_framework import serializers
from . import models


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = ('role_name',)


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Passport
        fields = ('numbers', 'series', 'registration_place', 'created_at')


class BirthSertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BirthSertificate
        fields = ('registration_place', 'place_of_birth', 'vital_record')


class ProfileSerializer(serializers.ModelSerializer):
    passport = PassportSerializer(many=False, read_only=True)
    birth_sertificate = BirthSertificateSerializer(many=False, read_only=True)
    class Meta:
        model = models.Profile
        fields = ('last_name', 'first_name', 'patronymic', 'sex', 'birth_date',
                  'phone', 'passport', 'birth_sertificate', 'address', 'image')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False, read_only=True)
    role = RoleSerializer(many=False, read_only=True)
    class Meta:
        model = models.User
        fields = ('id', 'email', 'profile', 'role')
