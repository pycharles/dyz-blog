from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from polls.models import Poll

#urlpatterns = patterns('polls.views',
#    url(r'^$', 'index'),
#    url(r'^(?P<poll_id>\d+)/$', 'detail'),
#    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
#    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
#)

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset = Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='detail.html')),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='results.html'),
            name='poll_results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)                      
                       
     
    
                       
                       
                       
                       
                       
                       
