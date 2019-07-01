from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices, bedroom_choices, price_choices


def index(request):
    listings = Listing.objects.order_by('-list_day').filter(is_published=True)[:3]
    context = {
        'state_choices': state_choices,
        'bedrooms_choices': bedroom_choices,
        'price_choices': price_choices,
        'latest_listings': listings
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    seller_of_the_month = realtors.filter(is_mvp=True).first()
    context = {
        'realtors': realtors,
        'seller_of_the_month': seller_of_the_month
    }
    return render(request, 'pages/about.html', context)


def register(request):
    return render(request, 'pages/about.html')


def login(request):
    return render(request, 'pages/about.html')
