# Generated by Django 4.2.5 on 2023-09-09 13:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_name",
                    models.CharField(
                        max_length=100,
                        validators=[django.core.validators.MaxLengthValidator(100)],
                    ),
                ),
                (
                    "review_text",
                    models.TextField(
                        max_length=200,
                        validators=[django.core.validators.MaxLengthValidator(200)],
                    ),
                ),
                (
                    "rating",
                    models.IntegerField(
                        max_length=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
            ],
        ),
    ]
