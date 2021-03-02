from rest_framework import serializers

from api.models import Comment, Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for posts."""

    class Meta:
        model = Post  # create new post
        fields = [  # list of required fields
            "id",
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
        ]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for comments."""

    class Meta:
        model = Comment  # create new comment
        fields = [
            "id",
            "post",
            "author_name",
            "content",
            "creation_date",
        ]  # list of required fields
