import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from dao.Database import read_Access


@api_view(['''GET'''])
def get_counters(request):
    return HttpResponse(json.dumps(read_Access('''counters'''), default=lambda o: o.__dict__), content_type='''application/json''')
