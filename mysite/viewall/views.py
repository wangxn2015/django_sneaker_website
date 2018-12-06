from django.shortcuts import render, redirect

# Create your views here.


def viewall(req):

    return redirect('/sneakers/')
    # return render(req, "viewall/viewall.html")