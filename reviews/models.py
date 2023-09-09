from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator


class Review(models.Model):
    user_name = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    review_text = models.TextField(max_length=200, validators=[MaxLengthValidator(200)])
    rating = models.IntegerField(max_length=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
