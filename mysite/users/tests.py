from django.test import TestCase
from users.models import MyUser, UserPermission
from django.contrib.auth.models import User
from django.contrib import auth
import datetime
from .models import Sneaker, MyUser, SubscriptionInfo
import login.views


class MyUserTestCase(TestCase):
    def setUp(self):
        permission = UserPermission.objects.create(userPermissionID=3, userType='user', modifyOtherAccount=0,
                                                   modifyPost=0)
        permission1 = UserPermission.objects.create(userPermissionID=2, userType='editor', modifyOtherAccount=0,
                                                    modifyPost=1)
        permission.save()
        permission1.save()
        user = User.objects.create_user(username='test1', password='123', email='test1@sleepless.com')
        user_profile = MyUser(user=user)
        user_profile.userCreateTime = datetime.date.today()
        user_profile.userBirthday = datetime.date(2018, 1, 1)
        user_profile.userDescription = 'i am user test1'
        obj = UserPermission.objects.filter(userPermissionID=2)
        user_profile.userPermissionID = obj[0]
        user_profile.save()

        user = User.objects.create_user(username='test2', password='123', email='test2@sleepless.com')
        user_profile = MyUser(user=user)
        user_profile.userCreateTime = datetime.date.today()
        user_profile.userBirthday = datetime.date(2018, 10, 10)
        user_profile.userDescription = 'i am user test2'
        obj = UserPermission.objects.filter(userPermissionID=3)
        print('obj:')
        print(obj)
        user_profile.userPermissionID = obj[0]

        user_profile.save()

    def test_myuser_create(self):
        user = User.objects.get(username='test1')
        user_id = user.id
        print('user2_id: %d' % user_id)
        test1 = MyUser.objects.get(user_id=user_id)
        user1_birth = test1.userBirthday
        user1_des = test1.userDescription

        user = User.objects.get(username='test2')
        user_id = user.id
        print('user2_id: %d' % user_id)
        test2 = MyUser.objects.get(user_id=user_id)
        user2_birth = test2.userBirthday
        user2_des = test2.userDescription

        self.assertEqual(test1.userDescription, user1_des)
        self.assertEqual(test2.userBirthday, user2_birth)

    def test_login(self):
        response = self.client.get('/login', follow=True)

        self.assertRedirects(response, '/login/', status_code=301, target_status_code=200)
        inputEmail = 'test2@sleepless.com'
        password = '123'

        response = self.client.post('/login/', {'inputEmail': inputEmail, 'inputPassword': password})
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_login_fail(self):
        response = self.client.get('/login', follow=True)

        self.assertRedirects(response, '/login/', status_code=301, target_status_code=200)
        inputEmail = 'test3@sleepless.com'
        password = '123'

        response = self.client.post('/login/', {'inputEmail': inputEmail, 'inputPassword': password}, follow=True)
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_register_(self):
        response = self.client.get('/register', follow=True)
        self.assertRedirects(response, '/register/', status_code=301, target_status_code=200)
        response = self.client.post('/register/', {'userName': 'a', 'inputEmail': 's@s.s', 'inputPassword': '123',
                                                   'repeatPassword': '123'}, follow=True)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_register_fail(self):
        response = self.client.get('/register', follow=True)
        self.assertRedirects(response, '/register/', status_code=301, target_status_code=200)
        response = self.client.post('/register/',
                                    {'userName': 'test1', 'inputEmail': 'test1@sleepless.com', 'inputPassword': '123',
                                     'repeatPassword': '123'}, follow=True)
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_logout(self):
        response = self.client.get('/login', follow=True)

        self.assertRedirects(response, '/login/', status_code=301, target_status_code=200)

        inputEmail = 'test2@sleepless.com'
        password = '123'
        response = self.client.post('/login/', {'inputEmail': inputEmail, 'inputPassword': password})
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

        response = self.client.get('/logout', follow=True)
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)
        self.assertRedirects(response, '/', status_code=301, target_status_code=200, fetch_redirect_response=True)


    def test_add_sneaker(self):

        response = self.client.get('/login', follow=True)

        self.assertRedirects(response, '/login/', status_code=301, target_status_code=200)
        inputEmail = 'test1@sleepless.com'
        password = '123'

        response = self.client.post('/login/', {'inputEmail': inputEmail, 'inputPassword': password})
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

        new = Sneaker()
        new.authorID = user
        new.title = "test"
        new.sneakerReleaseDate = '2018-02-01'
        new.price = 10
        new.store = ""
        new.storepic = ""
        new.url = ""
        new.reseller = ""
        new.resellerlink = "a"
        new.save()
        sneaker = Sneaker.objects.get(title="test")
        self.assertEqual(sneaker, new)

    def test_subscribe(self):
        response = self.client.get('/login', follow=True)

        self.assertRedirects(response, '/login/', status_code=301, target_status_code=200)
        inputEmail = 'test1@sleepless.com'
        password = '123'

        response = self.client.post('/login/', {'inputEmail': inputEmail, 'inputPassword': password})
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)
        new = Sneaker()
        new.authorID = user
        new.title = "test"
        new.sneakerReleaseDate = '2018-02-01'
        new.price = 10
        new.store = ""
        new.storepic = ""
        new.url = ""
        new.reseller = ""
        new.resellerlink = "a"
        new.save()
        response = self.client.post('/sneakers/subscribe/' + str(new.sneakerID) + '')
        try:
            SubscriptionInfo.objects.get(userID=user.id, sneakerID=new.sneakerID)
            self.assertTrue(True)
        except SubscriptionInfo.DoesNotExist:
            self.assertTrue(False)

