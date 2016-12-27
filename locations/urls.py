from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'CM_main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'list/$', views.list_locations, name='list'),
    url(r'view/(?P<lid>[0-9]+)/$', views.location_detail, name='detail'),
    url(r'add/$', views.add_location, name='add'),
    url(r'update/(?P<lid>[0-9]+)/$', views.update_location, name='update'),
    url(r'delete/(?P<lid>[0-9]+)/$', views.delete_location, name='delete'),
]
