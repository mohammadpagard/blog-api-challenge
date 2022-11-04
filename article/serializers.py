from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('id', 'body', 'updated')


class ArticleDetailSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
    
    def get_comment(self, obj):
        result = obj.comment.all()
        return CommentSerializer(instance=result, many=True).data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['owner', 'body']
