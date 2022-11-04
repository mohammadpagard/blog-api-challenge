# DRF packages
from rest_framework import generics
from .models import Article, Comment
# Local apps
from . import serializers


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleListSerializer


class ArticleDetailView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleDetailSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentDetailSerializer
