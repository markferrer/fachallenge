from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MovieReview(models.Model):
    title = models.CharField(max_length=255)
    mpaa_rating = models.CharField(max_length=5)
    critics_pick = models.IntegerField()
    headline = models.CharField(max_length=255)
    summary_short = models.TextField()

    # Log when this record was created and last modified in our DB.
    date_created_local = models.DateTimeField(auto_now_add=True)
    date_modified_local = models.DateTimeField(auto_now=True)

    email = models.EmailField(null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)


class Link(models.Model):
    movie_review = models.ForeignKey(MovieReview, on_delete=models.CASCADE)
    link_type = models.CharField(max_length=25)
    url = models.URLField()
    suggested_link_text = models.CharField(max_length=255)


class Multimedia(models.Model):
    movie_review = models.ForeignKey(MovieReview, on_delete=models.CASCADE)
    multimedia_type = models.CharField(max_length=25)
    src = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()
