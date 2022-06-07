from django.shortcuts import render
from django.http import HttpResponse
from api.models import Justices, Decisions;
from .decimalEncoder import DecimalEncoder
from .queries import DISENTING_JUSTICE_QUERY, DECISION_DURATION_QUERY, TERM_DURATION_QUERY
import json

def index(request):
    response_data = {};
    response_data['days'] = request.GET['d']
  
    for j in Decisions.objects.raw(DISENTING_JUSTICE_QUERY, [request.GET['d']]):
        response_data['disenting_justice'] = j.pretty_name;
    for d in Decisions.objects.raw(DECISION_DURATION_QUERY, [request.GET['d']]):
        response_data['decision_duration'] = d.average_duration;
    for j in Justices.objects.raw(TERM_DURATION_QUERY, [request.GET['d']]):
        response_data['term_duration'] = j.average_duration;
    return HttpResponse(json.dumps(response_data, cls=DecimalEncoder), content_type="application/json")
