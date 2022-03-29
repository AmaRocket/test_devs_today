# Generated by Django 4.0.3 on 2022-03-28 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=150)),
                ("link", models.URLField(max_length=250)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "amount_of_upvotes",
                    models.PositiveIntegerField(default=0, editable=False),
                ),
                (
                    "author_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to="news_board.author",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("content", models.TextField()),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "author_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="news_board.author",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="news_board.post",
                    ),
                ),
            ],
        ),
    ]