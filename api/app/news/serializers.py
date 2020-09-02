from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = [
            "title",
            "link", 
            "published",
            "description", 
            "author", 
            "language"
        ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5
                }
            }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        
        Token.objects.create(user=user)
        
        return user
