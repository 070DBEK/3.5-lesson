from rest_framework import serializers
from django.utils.text import slugify
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']
        extra_kwargs = {
            'slug': {'read_only': True}
        }

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if 'slug' not in data or not data['slug']:
            data['slug'] = slugify(data['name'])
        return data
