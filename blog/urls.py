from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.post_list, name='post_list'),
    url('^post/(?P<pk>[\w\-]+)/$', views.post_detail, name='post_detail'),
    url('^about/', views.about_me, name='about_me'),
    url('^home/', views.post_list, name='post_list'),
]