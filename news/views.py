from rest_framework import viewsets, response, status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import New
from .serializers import NewSerializer


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer

    def list(self, request, *args, **kwargs):
        count = self.get_queryset().count()
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response({
            "count": count,
            "results": serializer.data
        })

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        news = get_object_or_404(New, pk=pk)
        news.is_published = True
        news.save()
        return response.Response({"message": "Yangilik chop etildi"}, status=status.HTTP_200_OK)