from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_extensions.mixins import NestedViewSetMixin

from api.models import Comment, Post
from api.serializers import CommentSerializer, PostSerializer


class Comments(NestedViewSetMixin, viewsets.ModelViewSet):
    """Comments API."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class Posts(NestedViewSetMixin, viewsets.ModelViewSet):
    """Posts API."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class Upvotes(APIView):
    """Class that increases the number of votes for a post."""

    def get(self, request, post_id):
        """Function that get a post and increase votes."""

        post = Post.objects.filter(pk=post_id).first()  # get post by id

        if not post:
            return Response(
                {"error": "Post not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        post.add_vote()

        return Response({"message": "The post was upvoted."})
