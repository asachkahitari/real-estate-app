from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

from django.core.mail import send_mail
# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        name = request.POST['name']
        phone = request.POST['phone']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id = listing_id, user_id = user_id)
            if has_contacted:
                messages.error(request, 'You have already made an enquiry for this listing')
                return redirect('/listings/'+ listing_id)

        contact = Contact(listing = listing, listing_id = listing_id, name= name, email = email, phone= phone, message = message, user_id= user_id)
        contact.save()

        send_mail(
            'Property listing enquiry',
            'There was a enquiry from your end',
            'deeppak.21810454@viit.ac.in',
            [realtor_email, 'deepakpatilvnit@gmail.com'],
            fail_silently=False

        )

        messages.success(request, "Your query has been recorded. we will get back to you soon.")
        return redirect('/listings/'+ listing_id)
    return
