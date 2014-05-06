from django.shortcuts import render_to_response
import json
from chronos.models import Targets, PayloadBusComps
from django.db.models import Q

from webapp.appdata.sim_missions import missions

def homeTEST(request):
    js = {'status': 'Coming Soon...', 'response': 200, 'code': 0}
    js = json.dumps(js)
    
    params = {}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'
    params['status'] = js
    return render_to_response('webapp/homeTEST.html', params)

def start(request):
    tg = Targets.objects.all().filter(use_in_sim=True).order_by('name')
    params = {'targets': tg}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'

    return render_to_response('webapp/01-destinations.html', params)

def mission(request, p_slug):
    dt = Targets.objects.get(slug=p_slug)
    params = {'missions': missions, 'destination': p_slug}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'

    return render_to_response('webapp/02-mission.html', params)

def payload(request, p_slug, m_slug):
    pl = PayloadBusComps.objects.all().filter(category='payload')
    params = {'missions': missions, 'payloads': pl}
    params['keywords'] = 'explore space planets star journey satellites exploration solar system simulation play'

    return render_to_response('webapp/03-payload.html', params)
