from django.conf.urls import patterns, include, url
from ticker import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='index'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^search/$', 'ticker.views.search_ticker'),
    #url(r'^/$', 'ticker.views.tickers'),
    url(r'^(?P<symbol>\w+)/$', 'ticker.views.ticker'),
    url(r'^(?P<symbol>\w+)/ratios/$', 'ticker.views.ticker_ratio'),
    url(r'^(?P<symbol>\w+)/add_comment/$', 'ticker.views.add_comment'),
    url(r'^(?P<symbol>\w+)/(?P<id>\d+)/like/$', 'ticker.views.like_comment'),
)
