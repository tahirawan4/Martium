from django.http import HttpResponse
from django.http import JsonResponse
import json
import requests
from parser.constants import FEEDLY_API_URL, FEEDLY_GET_CATEGORIES_URL, DEV_TOKEN, FEEDLY_API_URL_IDS
from parser.utils import feed_parser


def index(request):
    feed_response_data = requests.get(FEEDLY_API_URL)
    data = json.loads(feed_response_data.text)
    return HttpResponse(json.dumps(feed_parser(data)), content_type="application/json")


def dash_board(request):
    feed_response_data = requests.get(FEEDLY_API_URL_IDS)
    data = json.loads(feed_response_data.text)
    return HttpResponse(json.dumps(data), content_type="application/json")


def get_categories(request):
    feed_response_data = requests.post(FEEDLY_GET_CATEGORIES_URL, headers={'authorization': DEV_TOKEN})
    data = json.loads(feed_response_data.text)
    return JsonResponse(json.dumps(data), safe=False)
