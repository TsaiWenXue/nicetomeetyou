from django.conf.urls import url

from . import views

app_name = 'news'

urlpatterns = [
    url(r'^$', views.news)
]