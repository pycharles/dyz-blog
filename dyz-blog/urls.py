from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

from django.contrib import admin
admin.autodiscover()

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,}

urlpatterns = patterns('',
	#url(r'^$','django.views.generic.simple.direct_to_template',{'template':'index.html'}, 'index'),
	url(r'^$','django.views.generic.simple.redirect_to',{'url':'/weblog/'}, 'index'),
    url(r'^polls/', include('polls.urls')),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^about$','django.views.generic.simple.direct_to_template',{'template':'about.html'},'base-about'),
    url(r'^contact$','common.views.contact',{},'base-contact'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index', {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)

#if settings.DEBUG :
#    urlpatterns += patterns('',
#        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#)
