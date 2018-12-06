from django.shortcuts import render
from users.models import Sneaker
import datetime
# Create your views here.


def upcoming(request):
    sneaker_list = Sneaker.objects.filter(sneakerReleaseDate__gte=datetime.date.today()).order_by('sneakerReleaseDate')
    return render(request, 'upcoming/upcoming.html', {
        'sneaker_list': sneaker_list
        })
