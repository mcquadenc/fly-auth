from rest_framework import serializers

from .models import FakeUser

class FakeUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FakeUser
        fields = ['name', 'email']