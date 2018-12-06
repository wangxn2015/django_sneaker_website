from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

import datetime
import django.utils.timezone as timezone


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userPermissionID = models.ForeignKey('UserPermission', on_delete=models.CASCADE)
    # banStatusID = models.IntegerField(default=0)
    userCreateTime = models.DateField(default=0)
    userBirthday = models.DateField(default=0)
    userDescription = models.CharField(max_length=100, default='test')


class UserPermission(models.Model):
    userPermissionID = models.IntegerField(primary_key=True)
    userType = models.CharField(max_length=100, default='user')
    modifyOtherAccount = models.BooleanField(default=False)
    modifyPost = models.BooleanField(default=False)


# class CommentBan(models.Model):
#     banID = models.IntegerField(primary_key=True)
#     userID = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     banEndDate = models.DateField(default=0)
#     banAddDate = models.DateField(default=0)


class Sneaker(models.Model):
    sneakerID = models.AutoField(primary_key=True)
    authorID = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="images", blank=True)
    sneakerReleaseDate = models.DateField()
    sneakerPublishDate = models.DateField(default=timezone.now)

    store = models.CharField(max_length=100, blank=True)
    storeimage = models.ImageField(upload_to="storeimages", blank=True, default="storeimages/blank.jpg")
    url = models.URLField(max_length=100, blank=True)
    price = models.IntegerField()
    color = models.CharField(max_length=100, default="TBD")
    stylecode = models.CharField(max_length=100, default="TBD")
    reseller = models.CharField(max_length=100, default="None")
    resellerlink = models.URLField(max_length=100, blank=True)


    # sneakerRating = models.FloatField(null=True)
    # sneakerLikeCount = models.IntegerField()


# def get_image_filename(instance, filename):
#     title = instance.sneaker.title
#     slug = slugify(title)
#     return "post_images/%s-%s" % (slug, filename)
#
# class Images(models.Model):
#     post = models.ForeignKey(Sneaker, default=None)
#     image = models.ImageField(upload_to=get_image_filename,
#                               verbose_name='Image')

#
# class SneakerPic(models.Model):
#     picID = models.IntegerField(primary_key=True)
#     # sneakerID = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
#     picName = models.CharField(max_length=100)
#     # picFile = models.CharField(max_length=100)
#     Image = models.ImageField(upload_to="mypictures", blank=True)
#
#     def __str__(self):
#         return self.picName
#
#     def get_absolute_url(self):
#         a = reverse('postnew:pic_detail', kwargs={'pk': self.picID})
#         print(a)
#         return a

# class RateSneaker(models.Model):
#     rateID = models.IntegerField(primary_key=True)
#     userID = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     sneakerID = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
#     ratingValue = models.FloatField(null=True)

class Store(models.Model):
    storeID = models.IntegerField(primary_key=True)
    storeName = models.CharField(max_length=100)
    storeType = models.CharField(max_length=100)
    storeWebsite = models.CharField(max_length=100)


class ShoppingInfo(models.Model):
    infoID = models.IntegerField(primary_key=True)
    sneakerID = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
    storeID = models.ForeignKey(Store, on_delete=models.CASCADE)
    buyLink = models.CharField(max_length=100)
    infoAddTime = models.DateField()


# class Comment(models.Model):
#     commentID = models.IntegerField(primary_key=True)
#     sneakerID = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
#     authorID = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     commentContent = models.CharField(max_length=100)
#     commentTime = models.DateField()


# class Reply(models.Model):
#     replyId = models.IntegerField(primary_key=True)
#     userID = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     commentID = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     content = models.CharField(max_length=1000)
#     replyAddTime = models.DateField()

# class Likes(models.Model):
#     commentID = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     userID = models.ForeignKey(MyUser, on_delete=models.CASCADE)

class SubscriptionInfo(models.Model):
    subInfoID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    sneakerID = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
    subDate = models.DateField()


