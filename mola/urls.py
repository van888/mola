from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mola.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^finance/', include('ticker.urls')),
    (r'^account/', include('userapp.urls')),
    (r'^search/', include('haystack.urls')),

)
