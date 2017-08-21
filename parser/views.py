from django.http import HttpResponse
import json


def index(request):
    # TODO: we will use serializers instead
    data = {'page': 'index'}
    return HttpResponse(json.dumps(data), content_type="application/json")
