from django.urls import path

from .views import (AuthorDetail, AuthorList, CommentDetail, CommentList,
                    PostUpvote, PostView, SinglePostView)

app_name = "news_board"

urlpatterns = [
    path("authors/", AuthorList.as_view()),
    path("authors/<int:pk>", AuthorDetail.as_view()),
    path("comments/", CommentList.as_view()),
    path("comments/<int:pk>", CommentDetail.as_view()),
    path("posts/", PostView.as_view()),
    path("posts/<int:pk>", SinglePostView.as_view()),
    path("upvote/<int:pk>/", PostUpvote.as_view()),
]
