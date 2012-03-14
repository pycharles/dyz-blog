from django.conf.urls.defaults import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','django.views.generic.simple.direct_to_template',{'template':'index.html'}, 'index'),
    url(r'^polls/', include('polls.urls')),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    

)

