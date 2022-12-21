from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('username is taken')
        return data

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'],
            email = validated_data['email'])
        user.set_password(validated_data['password'])
        return validated_data