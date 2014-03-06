from django.conf.urls import patterns, include, url
from ticker import views

urlpatterns = patterns(
    '',
    url(r'^login/$', 'userapp.views.login'),
    url(r'^auth/$', 'userapp.views.auth_view'),
    url(r'^logout/$', 'userapp.views.logout'),
    url(r'^loggedin/$', 'userapp.views.loggedin'),
    url(r'^invalid/$', 'userapp.views.invalid_login'),
    url(r'^register/$', 'userapp.views.register_user'),
    url(r'^register_success/$', 'userapp.views.register_success'),

)