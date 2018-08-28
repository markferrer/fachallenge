from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib import messages

from reviews.models import MovieReview

import requests
import json


class IndexView(ListView):
    template_name = 'reviews/index.html'
    model = MovieReview
    paginate_by = 1000

    def _get_movie_reviews(self):
        url = 'https://api.nytimes.com/svc/movies/v2/reviews/all.json'

        # TODO: Move API key out of code.
        payload = {
            'api-key': 'dc412bec38b24249b54658fbf5794b61'
        }

        # API only comes in results of 20
        # So we need to make more than one call to grab at least 1000 records.
        reviews = []
        for i in range(50):
            if i == 0:
                offset = 0
            else:
                offset = i * 20

            payload['offset'] = offset
            response = requests.get(url, params=payload)
            response.raise_for_status()

            data = response.json()

            results = data.get('results')

            if results:
                reviews.extend(results)

        return reviews

    def _save_reviews(self, reviews):
        for review in reviews:
            MovieReview.objects.get_or_create(
                title=review.get('display_title'),
                defaults = {
                    'mpaa_rating': review.get('mpaa_rating'),
                    'critics_pick': review.get('critics_pick'),
                    'headline': review.get('headline'),
                    'summary_short': review.get('summary_short')
                }
            )

    def get_queryset(self):
        return self.model.objects.all()[:100]

    def get_context_data(self, **kwargs):
        reviews = self._get_movie_reviews()
        self._save_reviews(reviews)

        ctx = super().get_context_data(**kwargs)
        return ctx
