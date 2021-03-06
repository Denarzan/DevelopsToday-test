# Generated by Django 3.0.6 on 2020-05-22 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("link", models.CharField(max_length=128, unique=True)),
                ("creation_date", models.DateTimeField(auto_now=True)),
                (
                    "amount_of_upvotes",
                    models.IntegerField(default=0, editable=False),
                ),
                ("author_name", models.CharField(max_length=64)),
            ],
            options={"ordering": ["creation_date"]},
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author_name", models.CharField(max_length=64)),
                ("content", models.TextField()),
                ("creation_date", models.DateTimeField(auto_now=True)),
                (
                    "post",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.Post",
                    ),
                ),
            ],
        ),
    ]
