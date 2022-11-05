# DRF packages
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Local apps
from .models import Article, Comment
from . import serializers
from . import permissions


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleListSerializer


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, permissions.IsOwnerOrReadOnly)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, permissions.IsOwnerOrReadOnly)
