from rest_framework import viewsets, response
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        count = self.get_queryset().count()
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response({
            "count": count,
            "results": serializer.data
        })