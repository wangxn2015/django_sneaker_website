from django.shortcuts import render, redirect
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.models import User
from users.models import MyUser, Sneaker
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers


class EmailBackend(ModelBackend):
    def authenticate(self,  email=None, password=None, **kwargs):
        try:
            # user = MyUser.objects.get(Q(username=username)|Q(email=username))
            user = User.objects.get(email=email)
            print('searching:')
            print(user)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None


def users(req):
    if req.method == 'GET':
        # get user
        print(req.user.username)
        user_name = req.user.username

        dir = '/users/'+user_name
        print(dir)
        return redirect(dir)


def user_detail(req, user_name):
    try:
        user = User.objects.get(username=user_name)
        id = user.id
        print(id)
        up = MyUser.objects.get(user_id=id)
        pid = up.userPermissionID_id
        print(pid)
        if pid == 2:
            editor_flag = True
        elif pid == 3:
            editor_flag = False
    except User.DoesNotExist:
        return None

    return render(req, "users/user_management.html", locals())


def user_profile(req, user_name):
    print(req.GET)
    print(user_name)
    try:
        user = User.objects.get(username=user_name)
        user_id = user.id
        print(user_id)
        up = MyUser.objects.get(user_id=user_id)
        # pid = up.userPermissionID_id
        # print(pid)
        user_birth = up.userBirthday
        user_des = up.userDescription
        len = 4
        context = {'len': len, 'user_id': user_id, 'user_name': user_name, 'user_birth': user_birth, 'user_des': user_des}
    except User.DoesNotExist:
        return None
    return JsonResponse(context)

    # return HttpResponse({'user_id': user_id, 'user_birth': user_birth, 'user_des': user_des})


def user_posts(req, user_name):
    user = User.objects.get(username=user_name)
    d_user_id = user.id
    # my_user = MyUser.objects.get(user_id=d_user_id)
    obj = Sneaker.objects.filter(authorID_id=user)
    print(obj)

    response = {}
    try:
        queryset = obj
        response['list'] = json.loads(serializers.serialize('json', queryset))
        response['status'] = 'success'
        response['error_num'] = 0
        print(response['list'])
    except Exception as e:
        response['status'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def user_edit_sneaker(req, user_name, sneaker_name):

    pass

def user_del_sneaker(request, user_name):

    if request.method == 'GET':
        sId = request.GET.get('id', 0)
        a = Sneaker.objects.get(pk=sId)
        print(sId)
        print('a:')
        print(a.authorID_id)
        print(request.user.id)
        if a.authorID_id == request.user.id:
        # if a.authorID == request.session['user_id']:
            a.delete()

        user = User.objects.get(username=user_name)
        # d_user_id = user.id
        obj = Sneaker.objects.filter(authorID_id=user)

        response = {}
        try:
            queryset = obj
            response['list'] = json.loads(serializers.serialize('json', queryset))
            response['status'] = 'success'
            response['error_num'] = 0
            print(response['list'])
        except Exception as e:
            response['status'] = str(e)
            response['error_num'] = 1
        return JsonResponse(response)


# def new_sneaker(req, user_name):
#
#     return render(req, "users/../postnew/templates/postnew/new.html", locals())

