from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.category, name='index'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    re_path(r'^inf_delete/(?P<id>\d+)/$', views.inf_delete, name='inf_delete'),
    re_path(r'^inf_update/(?P<id>\d+)/$', views.inf_update, name='inf_update'),
    re_path(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    re_path(r'^insert/(?P<id>\d+)/(?P<id2>\d+)/(?P<id3>\d+)/$', views.insert, name='insert'),
    re_path(r'^signup/$', views.signup, name='signup'),
];