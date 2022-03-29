from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author, Comment, Post
from .serializers import AuthorSerializer, CommentSerializer, PostSerializer


class AuthorList(ListCreateAPIView):
    """
    Simple view of authors list.
    """

    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        return queryset


class AuthorDetail(RetrieveUpdateDestroyAPIView):
    """
    Author details page.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class PostView(CreateAPIView, ListAPIView):
    """
    A simple ViewSet that for listing or retrieving posts.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        return serializer.save()


class SinglePostView(RetrieveUpdateDestroyAPIView):
    """
    Post detail page.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpvote(APIView):
    """
    UpVote post page.
    """

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post.objects.all(), pk=self.kwargs["pk"])
        post.upvote()
        return Response(
            data={"success": "Post is upvoted", "link": f"{post.link}"}, status=200
        )


class CommentList(ListCreateAPIView):
    """
    Simple view of comments list
    """

    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        post = self.request.query_params.get("post")

        if post:
            queryset = queryset.filter(post=post)
        return queryset

    def perform_create(self, serializer):
        return serializer.save()


class CommentDetail(RetrieveUpdateDestroyAPIView):
    """
    Comment details page
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
