from django.contrib import admin

# Register your models here.
from users.models import MyUser, UserPermission, Sneaker

# Register your models here.
admin.site.register(MyUser)
admin.site.register(UserPermission)
admin.site.register(Sneaker)
