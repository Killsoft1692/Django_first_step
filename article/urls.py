from django.conf.urls import url
from article import views

urlpatterns = [
    url(r'^basic/', views.basic),
    url(r'^articles/all/$', views.articles, name='all'),
    url(r'^articles/get/(?P<article_id>\d+)/$', views.article),
    url(r'^articles/addLike/(?P<article_id>\d+)/$', views.like),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment),
]
