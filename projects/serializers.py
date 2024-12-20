from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "owner",
        ]  # excluding auto-generated fieds + the owner can be retrieved from the request.user
