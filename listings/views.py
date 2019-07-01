from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Listing
from .choices import state_choices, bedroom_choices, price_choices


def index(request):
    listings_all = Listing.objects.order_by('-list_day').filter(is_published=True)
    paginator = Paginator(listings_all, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'page_listings': page_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    item = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': item
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    listings = Listing.objects.order_by('-list_day')
    # search params
    if 'keyword' in request.GET:
        keyword = request.GET['keywords']
        if keyword:
            listings = listings.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__icontains=city)
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            listings = listings.filter(state__icontains=state)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__exact=bedrooms)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__exact=price)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'state_choices': state_choices,
        'bedrooms_choices': bedroom_choices,
        'price_choices': price_choices,
        'search_result_page': page_listings,
        'params': request.GET
    }
    return render(request, 'listings/search.html', context)
