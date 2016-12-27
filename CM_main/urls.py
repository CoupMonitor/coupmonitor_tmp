from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from .views import home_view, about_view

urlpatterns = i18n_patterns(
    # Examples:
    # url(r'^$', 'CM_main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home_view, name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^locations/', include('locations.urls', namespace='locations')),
    url(r'^about/$', about_view, name='aboutpage'),
)
