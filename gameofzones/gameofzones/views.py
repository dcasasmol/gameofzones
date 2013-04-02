# Create yours views here.

from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    name = 'David'
    return render_to_response(
        'index.html', {'name': name}, context_instance=RequestContext(request))


def maintenance(request):
    return render_to_response('maintenance.html', {},
                              context_instance=RequestContext(request))
