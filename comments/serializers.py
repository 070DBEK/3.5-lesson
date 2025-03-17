from rest_framework import serializers
from .models import New, Comment


class CommentSerializer(serializers.ModelSerializer):
    new = serializers.PrimaryKeyRelatedField(queryset=New.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'new', 'author_name', 'author_email', 'content', 'is_approved', 'created_at']
        read_only_fields = ['is_approved']
