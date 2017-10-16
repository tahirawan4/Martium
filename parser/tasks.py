import json
import requests
from psycopg2._psycopg import IntegrityError

from parser.constants import FEEDLY_API_URL_CELERY, FEEDLY_ACCOUNT_TOKEN, FEEDLY_PRODUCTION_URL
from parser.models import Feed, Author, Keyword
from datetime import datetime
import datetime
from feedly.celery import app


def get_feed_content(streamId='feed/http://www.cnbc.com/id/10000115/device/rss/rss.html'):
    headers = {'Authorization': 'OAuth ' + FEEDLY_ACCOUNT_TOKEN}
    quest_url = "https://%s" % (FEEDLY_PRODUCTION_URL)
    quest_url += "/%s" % 'v3/streams/contents'
    params = dict(
        streamId=streamId,
        count=100
    )
    res = requests.get(url=quest_url, params=params, headers=headers)
    return res.json()


@app.task
def feed_importer(stream_id):
    # feed_url = FEEDLY_API_URL_CELERY
    data = get_feed_content()  # requests.get(feed_url)
    # data = json.loads(feed_response_data.text)
    for feed in data['items']:
        try:
            published_at = datetime.datetime.fromtimestamp(feed.get('published') / 1e3)
            feed_object, created = Feed.objects.get_or_create(feed_id=feed.get('id'))
            if not created:
                feed_object.engagement = feed.get('engagement', 0)
                feed_object.engagement_rate = feed.get('engagementRate', 0)
                feed_object.origin_url = feed.get('canonicalUrl', '')
                feed_object.save()
            else:
                author, _ = Author.objects.get_or_create(title=feed.get('author', '').lower())
                feed_object.author = author
                feed_object.title = feed.get('title', '')
                feed_object.origin_url = feed.get('canonicalUrl', '')

                feed_object.summary = feed.get('summary', '').get('content', '') if feed.get('summary', '') else ''
                feed_object.engagement = feed.get('engagement', 0)
                feed_object.engagement_rate = feed.get('engagementRate', 0)
                feed_object.published_at = published_at
                for keyword in feed.get('keywords', []):
                    keyword, _ = Keyword.objects.get_or_create(keyword=keyword.lower())
                    feed_object.keywords.add(keyword)
                feed_object.image = feed.get('visual', {}).get('url', '') if feed.get('visual', '') else '',
                feed_object.save()
        except IntegrityError:
            continue
