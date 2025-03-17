from rest_framework import viewsets, response, status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
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

    @action(detail=True, methods=['put'])
    def approve(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        comment.is_approved = True
        comment.save()
        serializer = self.get_serializer(comment)
        return response.Response(serializer.data, status=status.HTTP_200_OK)