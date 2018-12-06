from django.shortcuts import render

# Create your views here.


def aboutus(req):

    return render(req, "aboutus/aboutus.html")