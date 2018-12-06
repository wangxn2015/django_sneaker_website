from django.shortcuts import render
from users.models import Sneaker
# Create your views here.
import django
import datetime


def frontpage(req):
    print("django version: %s" % django.get_version())
    print("user now is:")
    print(req.user)
    sneaker_list = Sneaker.objects.filter(sneakerReleaseDate__gte=datetime.date.today()).order_by('sneakerReleaseDate')[:3]
    return render(req, "frontpage/frontpage.html", {
        'sneaker_list': sneaker_list
    })

