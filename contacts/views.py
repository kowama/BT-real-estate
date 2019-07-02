from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect

from .models import Contacts


def index(request):
    listing_id = request.POST['listing_id']
    if request.method == 'POST':
        listing_title = request.POST['listing_title']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            if Contacts.objects.filter(listing_id=listing_id, email=email).exists():
                messages.error(request, 'you already made this request !')
                return redirect('/listings/' + listing_id)

        contact = Contacts(listing_title=listing_title,
                           listing_id=listing_id,
                           name=name,
                           email=email,
                           phone=phone,
                           message=message)
        contact.save()

        send_mail(
            'BT Real Estate Property Listing Enquiry Request',
            f'Mr.s {name} with email : {email} is interested in this inquiry you publish here : {request.path}',
            'kowama.apptest@gmail.com',
            [realtor_email],
            fail_silently=True,
        )

        messages.success(request, 'Listings saved the realtor will get back to you soon !')
        return redirect('/listings/' + listing_id)
    return redirect('/listings/' + listing_id)
