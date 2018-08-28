from django.urls import path
from reviews.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]
