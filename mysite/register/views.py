from django.shortcuts import render, redirect
from users.models import MyUser, UserPermission

from django.contrib.auth.models import User
import datetime
from django.db import models
from django.contrib import auth
from users.views import EmailBackend
# from .forms import RegistrationForm, LoginForm, ProfileForm, PwdChangeForm
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required

# Create your views here.
# import django


def register(req):
    # print("django version: %s" % django.get_version())
    if req.method == 'POST':
        message = 'please recheck your information'
        username = req.POST.get("userName", None)
        email = req.POST.get("inputEmail", None)
        passwd = req.POST.get("inputPassword", None)
        passwd2 = req.POST.get("repeatPassword", None)
        if passwd != passwd2:
            message = 'password are different'
            return render(req, 'register/register.html', locals())
        else:
            if not User.objects.all().filter(email=email):
                if not User.objects.all().filter(username=username):
                    # 使用内置User自带create_user方法创建用户，不需要使用save()
                    user = User.objects.create_user(username=username, password=passwd, email=email)
                    # 如果直接使用objects.create()方法后不需要使用save()
                    user_profile = MyUser(user=user)
                    user_profile.userCreateTime = datetime.date.today()
                    user_profile.userBirthday = datetime.date(2017, 3, 22)
                    user_profile.userDescription = 'i am what i am'
                    # user_profile.userPermission = UserPermission.objects.create(
                    #     userPermissionID_id=3,
                    #     userType='user',
                    #     modifyOtherAccount=False,
                    #     modifyPost=False,
                    # )
                    obj = UserPermission.objects.filter(userPermissionID=3)
                    user_profile.userPermissionID = obj[0]
                    # user_profile.userPermissionID_id = 3
                    user_profile.save()

                    mailname = EmailBackend()
                    user = mailname.authenticate(email=email, password=passwd)
                    print(user)
                    if user and user.is_active:
                        auth.login(req, user, backend='users.views.EmailBackend')
                        name = user.username
                        print("user name: %s" % name)

                    # return render_to_response('member.html', {'username': username})
                    return redirect('/')
                return render(req, 'register/register.html', {'message': 'username already exists'})
            return render(req, 'register/register.html', {'message': 'user email already exists'})

    return render(req, "register/register.html")
