from django.shortcuts import render
from django.http import HttpResponse
from api.models import Justices, Decisions;
import json

DISENTING_JUSTICE_QUERY = "SELECT 1 AS id, pretty_name FROM decisions WHERE datedecision > ('1791-08-03'::DATE +  make_interval(0,0,0,%s)) AND majority = '1' GROUP BY pretty_name ORDER BY count(*) DESC limit 1";

DECISION_DURATION_QUERY = "SELECT 1 AS id, ROUND(AVG(EXTRACT(EPOCH FROM AGE(datedecision, dateargument))/(60*60*24)),2) AS average_duration FROM decisions WHERE datedecision > ('1791-08-03'::DATE +  make_interval(0,0,0,%s))";

TERM_DURATION_QUERY = "SELECT 1 AS id, COALESCE(ROUND(AVG(EXTRACT(EPOCH FROM AGE(finish_date, start_date))/31557600),1)::TEXT, 'No Data')  AS average_duration FROM justices WHERE is_active='false' AND start_date > ('1791-08-03'::DATE +  make_interval(0,0,0,%s))";
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

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
