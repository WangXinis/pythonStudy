"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import re_path as url
from django.contrib import admin
from boards import views
urlpatterns =[
    url(r'^home$', views.home,name="home"),
    url(r'^/$', views.home,name="home"),
    url("^/$",views.index,name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^time/plus/(\d{1,2})/$',views.hours_head,name="hours_head"),
    url(r'^display_meta$',views.display_meta,name="display_meta"),
    url(r'^search_form$',views.search_form,name="search-form"),
    url(r'^search/$',views.search,name="search"),
    url(r'^current_url$',views.current_url,name="current_url"),
    url(r'^current_ip$',views.current_ip,name="current_url"),

]
