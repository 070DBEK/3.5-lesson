from .models import Category
from rest_framework import serializers
# from django.utils.text import slugify


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'slug']
        extra_kwargs = {
            'slug': {'read_only': True}
        }

        # def to_internal_value(self, data):
        #     data = super().to_internal_value(data)
        #     if 'slug' not in data or not data['slug']:
        #         data['slug'] = slugify(data['name'])
        #     return data


