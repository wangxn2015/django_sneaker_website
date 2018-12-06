from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView
from . import views

urlpatterns = [
    path('', views.sneakers, name='sneakers'),
    path('search/', views.search, name='search'),
    path('new/', views.newsneaker, name='newsneaker'),
    path('<int:sneaker_id>/', views.sneaker_detail, name='one_sneaker'),
    path('subscribe/<int:sneaker_id>',views.sneaker_subscribe,name='subscribe'),
    url(r'^restapi/$', CreateView.as_view(), name="create"),
    url(r'^restapi/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    path('management/', views.management, name='management'),
    path(r'delsneaker/', views.delsneaker, name='delsneaker'),
    path(r'editsneaker/', views.editsneaker, name='editsneaker'),
]