from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Review


class ReviewView(CreateView):
    model = Review
    fields = '__all__'
    template_name = 'reviews/review.html'
    success_url = '/thank-you'


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context


class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'  # by default: object_list


class ReviewDetailView(DetailView):
    template_name = 'reviews/review-detail.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get('favorite_review')
        context['is_favorite'] = favorite_id == str(loaded_review.id)
        return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect(reverse('review-detail', args=[review_id]))
