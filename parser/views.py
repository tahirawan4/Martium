from django.http import HttpResponse
from django.http import JsonResponse
import json
import requests
from parser.constants import FEEDLY_API_URL, FEEDLY_GET_CATEGORIES_URL, DEV_TOKEN, FEEDLY_API_URL_IDS,TEXT_RAZOR_API_KEY
from parser.utils import feed_parser
from parser import feeds_dictionary
from parser.models import Feed
from django.core.paginator import Paginator
from parser.tasks import feed_importer
from textrazor import TextRazor

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
    result = feed_importer(stream_id)
    return JsonResponse({'success':True}, safe=False)


def text_razor(request):


    # This restores the same behavior as before.
    import textrazor

    fed_obj = Feed.objects.filter(is_hidden=False).first()
    fed  = fed_obj.summary

    print("fed",fed)
    client = TextRazor(TEXT_RAZOR_API_KEY, extractors=["entities","topics"])
    client.set_classifiers(["textrazor_newscodes"])
    manager = textrazor.ClassifierManager()
    response = client.analyze(fed)
    for category in response.categories():
        print ("dfsdf",category.category_id, category.label, category.score)



    for topics in response.topics():
        print ("topics", topics.label, topics.score)
    # csv_contents = file("sports_classifier.csv").read().decode("utf-8")
    # manager.create_classifier_with_csv("my_sports", csv_contents)

    # textrazor.api_key = TEXT_RAZOR_API_KEY
    # #
    # text = "Barclays misled shareholders and the public about one of the biggest investments in the bank's history, a BBC Panorama investigation has found"
    # manager = textrazor.ClassifierManager()
    # test_classifier_id = text.encode("utf-8")
    # for category in manager.all_categories(test_classifier_id).categories:
    #     print("category",category.query)
    #
    return JsonResponse({'success': True}, safe=False)