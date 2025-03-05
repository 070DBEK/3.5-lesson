from rest_framework import viewsets, response
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