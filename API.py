import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from dao.Database import ReadDB


@api_view(['''GET'''])
def get_counters(request):
    return HttpResponse(json.dumps(ReadDB(), default=lambda o: o.__dict__), content_type='''application/json''')
