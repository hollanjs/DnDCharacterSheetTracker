from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^characters/$', views.CharacterList.as_view(), name='character_list'),
    url(r'^characters/(?P<pk>[0-9]+)/$', views.CharacterDetail.as_view(), name='character_detail'),
]