from django.shortcuts import render, redirect

from django.contrib import auth


def logout(req):
    auth.logout(req)
    return redirect('/')



