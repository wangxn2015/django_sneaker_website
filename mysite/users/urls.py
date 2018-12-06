from django.urls import path

from . import views

urlpatterns = [
    path('', views.users, name='users'),
    # path('<str:user_name>/', views.user_detail, name='user'),
    path('<str:user_name>/', views.user_detail, name='user'),
    path('<str:user_name>/profile/', views.user_profile, name='user_profile'),
    path('<str:user_name>/posts/', views.user_posts, name='user_posts'),
    # path('<str:user_name>/posts/new/', views.new_sneaker, name='user_pose_sneaker'),
    path('<str:user_name>/posts/<str:sneaker_name>/', views.user_edit_sneaker, name='user_edit_sneaker'),
    path('<str:user_name>/delete/', views.user_del_sneaker, name='user_del_sneaker'),

]