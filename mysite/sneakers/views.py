from django.shortcuts import render, redirect
from sneakers.sneakerform import SneakerForm
from users.models import Sneaker
from django.http import HttpResponse
from django.contrib.auth.models import User
import datetime
from django.db.models import Q
from rest_framework import generics
from .serializers import SneakerSerializer
from .models import Sneaker, MyUser, SubscriptionInfo
from django.shortcuts import render
from django.db import models


def sneakers(request):

    # userId = request.session.get('user_id')
    list = Sneaker.objects.filter().order_by('-sneakerReleaseDate')
    return render(request, 'sneakers/sneakerlist.html', {'sneakers': list})

def management(request):

    user_name = request.user
    # print(user_name)
    # list = Sneaker.objects.filter().order_by('-sneakerReleaseDate')
    user = User.objects.get(username=user_name)
    d_user_id = user.id
    obj = Sneaker.objects.filter(authorID_id=d_user_id)
    # print(obj)

    return render(request, 'sneakers/sneaker_management.html', {'sneakers': obj})


def newsneaker(request):

    user_name = request.user
    user = None
    try:
        user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        return redirect('/')

    id = user.id
    print(id)
    up = MyUser.objects.get(user_id=id)
    pid = up.userPermissionID_id
    print(pid)
    if pid == 2:
        sneakerform = SneakerForm()
        if request.method == 'GET':
            # sneakerform = SneakerForm()
            return render(request, 'sneakers/new.html', {'sneakerform': sneakerform})
        elif request.method == 'POST':
            submitForm = SneakerForm(request.POST, request.FILES)
            if submitForm.is_valid():
                # new = Sneaker(sneakerReleaseDate=submitForm.cleaned_data['releaseDate'])
                new = Sneaker()
                new.image = submitForm.cleaned_data['pic']
                new.title = submitForm.cleaned_data['title']
                new.body = submitForm.cleaned_data['content']
                new.sneakerReleaseDate = submitForm.cleaned_data['sneakerReleaseDate']
                # new.publishDate = submitForm.cleaned_data['publishDate']
                new.color = submitForm.cleaned_data['color']
                new.price = submitForm.cleaned_data['price']
                new.store = submitForm.cleaned_data['store']
                new.storepic = submitForm.cleaned_data['storepic']
                new.url = submitForm.cleaned_data['url']
                new.reseller = submitForm.cleaned_data['reseller']
                new.resellerlink = submitForm.cleaned_data['resellerlink']

                tmpt = request.user.username
                user = User.objects.get(username=tmpt)
                new.authorID = user
                # print(new.authorID)
                # print('releaseDate:')
                # print(type(new.sneakerReleaseDate))
                # print(new.sneakerReleaseDate)
                new.save()
                return render(request, 'sneakers/new.html', {'sneakerform': sneakerform, 'message': 'post successfully.'})
            else:
                return render(request, 'sneakers/new.html', {'sneakerform': submitForm})
    elif pid == 3:
        return redirect('/')

def sneaker_subscribe(request, sneaker_id):
    if not request.user.is_authenticated:

        return redirect('/login')
    if request.method == 'POST':
        sneaker = Sneaker.objects.get(pk=sneaker_id)
        try:
            SubscriptionInfo.objects.get(userID=request.user.id, sneakerID=sneaker_id).delete()
        except SubscriptionInfo.DoesNotExist:
            user = request.user
            new = SubscriptionInfo()
            new.userID = user
            new.sneakerID = sneaker
            new.subDate = datetime.date.today()
            new.save()
        return redirect('/sneakers/'+str(sneaker_id)+'/')


def sneaker_detail(req, sneaker_id):

    sneaker = Sneaker.objects.get(pk=sneaker_id)
    try:
        new = SubscriptionInfo.objects.get(userID=req.user.id, sneakerID=sneaker_id)
        return render(req, "sneakers/sneakerdetail.html", {'sneaker': sneaker, 'subscribe_info': "Subscribed"})

    except SubscriptionInfo.DoesNotExist:
        return render(req, "sneakers/sneakerdetail.html", {'sneaker': sneaker, 'subscribe_info': "Click to Subscribe"})


def search(request):
    q = request.POST.get('q', '')
    sneaker_list = Sneaker.objects.filter(Q(title__icontains=q) | Q(body__icontains=q)).order_by('sneakerReleaseDate')
    return render(request, 'sneakers/search.html', {
        'sneaker_list': sneaker_list
    })


class CreateView(generics.ListCreateAPIView):
    queryset = Sneaker.objects.all()
    serializer_class = SneakerSerializer

    def perform_create(self, serializer):
        serializer.save(authorID=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Sneaker.objects.all()
    serializer_class = SneakerSerializer


def editsneaker(request):
    user_name = request.user
    user = None
    try:
        user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        return redirect('/')

    id = user.id
    print(id)
    up = MyUser.objects.get(user_id=id)
    pid = up.userPermissionID_id
    print(pid)
    if pid == 2:
        if request.method == 'GET':
            sId = request.GET.get('id', 0)
            print("sId:"+str(sId))
            sneaker = Sneaker.objects.get(pk=sId)
            sneakerform = SneakerForm(initial={
                'title': sneaker.title,
                'content': sneaker.body,
                'pic': sneaker.image,
                'sneakerReleaseDate': sneaker.sneakerReleaseDate,
                'color': sneaker.color,
                'price': sneaker.price,
                'store': sneaker.store,
                'storepic': sneaker.storeimage,
                'url': sneaker.url,
                'reseller': sneaker.reseller,
                'resellerlink': sneaker.resellerlink,
            })
            return render(request, 'sneakers/edit.html', {'sneakerform': sneakerform, 'id': sId})

        elif request.method == 'POST':
            submitForm = SneakerForm(request.POST, request.FILES)
            print('POST:')
            print(request.POST)
            tid = request.POST.get('id', 0)
            print('id:'+str(tid))
            if submitForm.is_valid():
                # user_id = request.session['user_id']
                ups = Sneaker.objects.get(sneakerID=tid)
                print('ups:')
                print(ups)
                ups.image = submitForm.cleaned_data['pic']
                ups.title = submitForm.cleaned_data['title']
                ups.body = submitForm.cleaned_data['content']
                ups.sneakerReleaseDate = submitForm.cleaned_data['sneakerReleaseDate']
                # new.publishDate = submitForm.cleaned_data['publishDate']
                ups.color = submitForm.cleaned_data['color']
                ups.price = submitForm.cleaned_data['price']
                ups.store = submitForm.cleaned_data['store']
                ups.storepic = submitForm.cleaned_data['storepic']
                ups.url = submitForm.cleaned_data['url']
                ups.reseller = submitForm.cleaned_data['reseller']
                ups.resellerlink = submitForm.cleaned_data['resellerlink']

                tmpt = request.user.username
                user = User.objects.get(username=tmpt)
                ups.authorID = user
                # print(new.authorID)
                # print('releaseDate:')
                # print(type(new.sneakerReleaseDate))
                # print(new.sneakerReleaseDate)
                aa = ups.save()
                print(aa)
                return redirect('/users/')  # 重定向到博客首页
            else:
                print('not valid')
                return render(request, 'sneakers/edit.html', {'sneakerform': submitForm, 'id': tid})
    elif pid == 3:
        return redirect('/')


def delsneaker(request):
    # isPassed,next=checkLogin(request.session)
    # if not isPassed:
    #     return next
    if request.method == 'GET':
        sId = request.GET.get('id', 0)
        a = Sneaker.objects.get(pk=sId)
        print('sId:')
        print(sId)
        # print('a:')
        # print(a.authorID_id)
        # print(request.user.id)
        if a.authorID_id == request.user.id:
        # if a.authorID == request.session['user_id']:
            a.delete()
            return redirect('/sneakers/management/')
        else:
            return HttpResponse('sorry, error occurs')

