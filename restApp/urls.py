from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from rest_framework.urlpatterns import format_suffix_patterns
from restApp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    #url(r'^$','index_view',name='vista_home'),
    #url(r'^prueba','prueba',name='prueba'),
    url(r'^', include(router.urls)),
    url(r'^polls/$', views.poll_list.as_view()),
    url(r'^polls/(?P<pk>[0-9]+)/$', views.poll_detail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)


#urlpatterns = format_suffix_patterns(urlpatterns)