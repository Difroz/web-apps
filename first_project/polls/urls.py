from django.urls import re_path

from . import views

app_name = 'polls'
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^(?P<pk>[-\w]+)/$', views.DetailsView.as_view(), name='detail'),
    re_path(r'^(?P<pk>[-\w]+)/result/$', views.ResultView.as_view(), name='result'),
    re_path(r'^(?P<question_id>[-\w]+)/vote/$', views.vote, name='vote')
]
