from django.urls import path

from . import views

urlpatterns = [
    path('', views.viewall, name='viewall'),

]