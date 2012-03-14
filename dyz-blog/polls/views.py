from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

from polls.models import Poll, Choice

#Only the vote view is being used since changed to generic views
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]

    return render_to_response('index.html',
                {'latest_poll_list': latest_poll_list,})

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
        
    return render_to_response('detail.html',
                {'poll': poll,},
                context_instance=RequestContext(request))

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('results.html',
                {'poll': poll,},
                context_instance=RequestContext(request))

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the poll voting form
        return render_to_response("polls/detail.html",
                {'poll':poll,
                'error_message': "You didn't select a choice.",                                                       
                }, context_instance=RequestContext(request))
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('poll_results', args=(poll.id,)))
    
    
    