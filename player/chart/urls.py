from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/index$', views.IndexView.as_view()),
    url(r'^/rank/(?P<name>\w+)/(?P<start>\d+)/(?P<end>\d+)$',views.RankView.as_view()),
    url(r'^/find$', views.FindView.as_view()),
    url(r'^/findserver',views.find_server)
]