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
from parser.constants import feedly_api_url,feedly_get_categories_url,feedly_authrization_url,dev_token,client_id


def index(request):
    # TODO: we will use serializers instead
    feed_response_data = requests.get(feedly_api_url)

    data = feed_response_data.text

    return HttpResponse(json.dumps(data), content_type="application/json")


def dash_board(request):
    # TODO: This view is call from the url and will return the Feedly fetch records to html view
    # url(r'^dashboard$', dash_board, name='dash_board'),

    feed_response_data = requests.get(feedly_api_url)

    data = feed_response_data.text
    return JsonResponse(data, safe=False)


def get_categories(request):
    # TODO: This view is call from the url and will return the Feedly fetch records to html view
    # url(r'^dashboard$', dash_board, name='dash_board'),

    feed_response_data = requests.post(feedly_get_categories_url, headers = {'authorization': dev_token})


    # feed_response_data = requests.get(feedly_get_categories_url)


    data = feed_response_data.text
    return JsonResponse(data, safe=False)
