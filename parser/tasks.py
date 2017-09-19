import json

import requests

from parser.constants import FEEDLY_API_URL
from parser.models import Feed, Author, Keyword
from datetime import datetime


def feed_importer(stream_id):
    feed_url = FEEDLY_API_URL % stream_id
    feed_response_data = requests.get(feed_url)
    data = json.loads(feed_response_data.text)

    for feed in data['items']:
        feed_object, created = Feed.objects.get_or_create(id=feed.get('id'))
        if not created:
            feed_object.update(engagement=feed.get('engagement', 0), engagement_rate=feed.get('engagementRate', 0))
        else:
            author, _ = Author.objects.get_or_create(title=feed.get('author', '').lower())
            feed_object.author = author
            feed_object.title = feed.get('title', '')
            feed_object.origin_url = feed.get('originId', '')
            feed_object.published_at = feed.get('published', datetime.now())
            feed_object.summary = feed.get('summary', '').get('content', '') if feed.get('summary', '') else ''
            feed_object.engagement = feed.get('engagement', 0)
            feed_object.engagement_rate = feed.get('engagementRate', 0)
            # 'stream_id': feed.get('origin', '').get('streamId', '') if feed.get('origin', '') else '',
            # 'image': feed.get('visual', '').get('url', '') if feed.get('visual', '') else '',
            for keyword in feed.get('keywords', []):
                keyword, _ = Keyword.objects.get_or_create(keyword=keyword.lower())
                feed_object.keywords.add(keyword)
            feed_object.save()
