from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from users.models import User


# Signup serializer
class SignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        # Ensuring password hashing
        return User.objects.create_user(**validated_data)
