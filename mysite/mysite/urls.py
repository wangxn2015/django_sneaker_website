"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
# from . import views
# from frontpage import views as fpviews

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', include('login.urls')),

    path('', include('frontpage.urls'), name='index'),

    path('aboutus/', include('aboutus.urls')),

    path('upcoming/', include('upcoming.urls')),

    path('viewall/', include('viewall.urls')),

    path('register/', include('register.urls')),

    path('users/', include('users.urls')),

    path('logout/', include('logout.urls')),

    # path('postnew/', include('postnew.urls')),

    path('sneakers/', include('sneakers.urls')),
    # path('', fpviews.frontpage),
    # path('frontpage/', include('frontpage.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
