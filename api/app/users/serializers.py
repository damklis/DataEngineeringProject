from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import UserModel


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ("email", "password")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 5
                }
            }

    def create(self, validated_data):
        user = UserModel(
            email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        
        Token.objects.create(user=user)
        
        return user
