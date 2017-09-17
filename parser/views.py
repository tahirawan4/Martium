from django.http import HttpResponse
import json

# def index(request):
#     # TODO: we will use serializers instead
#     data = {'page': 'index'}
#     return HttpResponse(json.dumps(data), content_type="application/json")



from django.http import HttpResponse
from django.http import JsonResponse
import json
import requests
from parser.constants import FEEDLY_API_URL, FEEDLY_GET_CATEGORIES_URL, DEV_TOKEN, CLIENT_ID, FEEDLY_API_URL_IDS


def index(request):
    # TODO: we will use serializers instead
    feed_response_data = requests.get(FEEDLY_API_URL)

    data = json.loads(feed_response_data.text)
    return HttpResponse(json.dumps(data), content_type="application/json")


def dash_board(request):
    # TODO: This view is call from the url and will return the Feedly fetch records to html view
    # url(r'^dashboard$', dash_board, name='dash_board'),

    feed_response_data = requests.get(FEEDLY_API_URL_IDS)

    data = json.loads(feed_response_data.text)
    return HttpResponse(json.dumps(data), content_type="application/json")


def get_categories(request):
    # TODO: This view is call from the url and will return the Feedly fetch records to html view
    # url(r'^dashboard$', dash_board, name='dash_board'),

    feed_response_data = requests.post(FEEDLY_GET_CATEGORIES_URL, headers={'authorization': DEV_TOKEN})

    # feed_response_data = requests.get(feedly_get_categories_url)


    data = feed_response_data.text
    return JsonResponse(data, safe=False)
