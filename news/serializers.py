from rest_framework import serializers
from .models import New, Category, Tag
from django.utils.text import slugify


class NewSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = New
        fields = [
            'id', 'title', 'slug', 'content', 'category', 'tags', 'image',
            'views_count', 'is_published', 'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'slug': {'read_only': True}
        }

        def to_internal_value(self, data):
            data = super().to_internal_value(data)
            if 'slug' not in data or not data['slug']:
                data['slug'] = slugify(data['title'])
            return data
