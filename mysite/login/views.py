from django.shortcuts import render, redirect

import django
from . import models
from django.contrib import auth
from users.views import EmailBackend

# from .forms import UserForm
# user_list = []


def login(req):
    # print("django version: %s" % django.get_version())
    if req.method == "POST":
        email = req.POST.get("inputEmail", None)
        password = req.POST.get("inputPassword", None)
        message = 'please check what you input'
        print(email)
        print(password)
        if email and password:
            # user = auth.authenticate(email=email, password=password)
            mailname = EmailBackend()
            user = mailname.authenticate(email=email, password=password)
            print(user)
            if user and user.is_active:
                auth.login(req, user, backend='users.views.EmailBackend')
                name = user.username
                print(name)
                # return redirect('/frontpage', {'name': username})
                return redirect('/')

            else:
                message = 'No such user or Wrong password'
                # return render(req, 'login/login.html', {'message': 'Wrong password. Please try again.'})
                return render(req, 'login/login.html', {'message': message})

        # if email and password:
        #     # email = email.strip()
        #     try:
        #         user = models.User.objects.get(name=email)
        #         if user.password == password:
        #             return redirect('/frontpage')
        #         else:
        #             message = "password is wrong"
        #     except:
        #         message = "user email doesn't exist"
        # return render(req, 'login/login.html', locals())
            # return render(req, 'login/login.html', {"message": message})

        # user = {'username': username, 'email': email}
        # user_list.append(user)
        # return render(req, "login/login.html", {'user_list': user_list})
    return render(req, "login/login.html")


def admin(req):

    return render(req, "login/admin1.html")

