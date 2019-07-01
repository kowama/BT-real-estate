from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Listing


def index(request):
    listings_all = Listing.objects.order_by('-list_day').filter(is_published=True)
    paginator = Paginator(listings_all, 12)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'page_listings': page_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    item = Listing.objects.get(id=listing_id)
    context = {
        'listing': item
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
