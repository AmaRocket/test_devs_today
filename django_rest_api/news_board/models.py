from django.db import models


class Author(models.Model):
    """
    Author table.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class PostManager(models.Manager):
    """
    Post manager.
    """

    def created(self):
        return self.order_by("-creation_date")

    def by_user(self, user):
        return self.filter(author=user).order_by("-creation_date")


class Post(models.Model):
    """
    Post table.
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.PositiveIntegerField(default=0, editable=False)
    author_name = models.ForeignKey(
        "Author", related_name="posts", on_delete=models.CASCADE
    )

    objects = PostManager()

    def __str__(self):
        return self.title

    def upvote(self):
        self.amount_of_upvotes += 1
        self.save()

    @classmethod
    def reset_upvotes(Post):
        print("Resetting post upvotes count...")
        Post.objects.all().update(upvotes_amount=0)
        print("Post upvotes count has been reseted")


class Comment(models.Model):
    """
    Comment table.
    """

    id = models.AutoField(primary_key=True)
    author_name = models.ForeignKey(
        "Author", related_name="comments", on_delete=models.CASCADE
    )
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author_name}"
