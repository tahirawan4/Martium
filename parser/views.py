from django.http import HttpResponse
from django.http import JsonResponse
import json
import requests
from parser.constants import FEEDLY_API_URL, FEEDLY_GET_CATEGORIES_URL, DEV_TOKEN, FEEDLY_API_URL_IDS
from parser.utils import feed_parser
from parser import feeds_dictionary
from parser.models import Feed
from parser.tasks import feed_importer


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


def get_feeds(request):
    limit = request.GET.get('limit')if 'limit' in request.GET else 10
    feeds_list = []
    feeds_obj = Feed.objects.filter(is_hidden=False)[0:int(limit)]

    for feeds in feeds_obj:
        feeds_list.append(feeds_dictionary(feeds))

    return JsonResponse(json.dumps(feeds_list), safe=False)


def start_task(request):
    stream_id = request.GET.get('stream_id')
    result = feed_importer.delay(stream_id)
    return JsonResponse({'success':True}, safe=False)