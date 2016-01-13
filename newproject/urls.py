"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from newproject.views import home
# from django.core.urlresolvers import reverse

import views
# from views import check1
# from views import post

urlpatterns = [
	url(r'^$', home , name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^check/$', views.check1 , name="homefile"),
    url(r'^contact/$',views.contact, name= "contact"),
    url(r'^articles/$',views.articles, name= "articles"),
    url(r'^register/$',views.register , name="register"),
    url(r'^create/$',views.create),
    url(r'^reachhome/$',views.reachhome,name="reachhome"),
    url(r'^change1/$',views.change1,name="change1"),
    url(r'^change/$',views.change, name="change"),
    url(r'^reach/$',views.reach, name= "reach"),
    url(r'^search/$',views.search),
	url(r'(?P<slug>\S+)/$', views.post),

]
