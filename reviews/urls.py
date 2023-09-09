from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewView.as_view(), name='review'),
    path('thank-you', views.ThankYouView.as_view(), name='thank-you'),
    path('reviews', views.ReviewsListView.as_view(), name='reviews-list'),
    path('reviews/<int:id>', views.ReviewDetailView.as_view(), name='review-detail')
]
