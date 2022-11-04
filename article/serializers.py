from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        exclude = ('id', 'body', 'updated')


class ArticleDetailSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
    
    def get_comment(self, obj):
        result = obj.comment.all()
        return CommentSerializer(instance=result, many=True).data


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['owner', 'body']


class CommentDetailSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    article = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
