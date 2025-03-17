from rest_framework import viewsets, response, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import New
from .serializers import NewSerializer


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):
        count = self.get_queryset().count()
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response({
            "count": count,
            "results": serializer.data
        })

    @action(detail=True, methods=['put'])
    def publish(self, request, slug=None):
        news = get_object_or_404(New, slug=slug)
        news.is_published = True
        news.save()
        return Response({"message": "News published successfully!"}, status=status.HTTP_200_OK)
