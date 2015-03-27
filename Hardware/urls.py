from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Hardware.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'', include('baza.urls')),
    url(r'', include('pracownicy.urls')),
    url(r'', include('wnioski.urls')),
    url(r'', include('koszty.urls'))
)

