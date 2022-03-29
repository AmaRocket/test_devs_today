from rest_framework.serializers import ModelSerializer

from .models import Author, Comment, Post


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
            "comments",
        )
        read_only_fields = ["comments"]


class PostUpvoteSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):
        fields = ("id", "amount_of_upvotes")
