from celery import shared_task

from .models import Post


@shared_task
def reset_post_upvotes():
    Post.reset_upvotes()
