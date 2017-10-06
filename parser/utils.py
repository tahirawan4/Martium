from ast import literal_eval as make_tuple


def feed_parser(feeds):
    feeds_data = []
    for feed in feeds['items']:
        feeds_data.append({
            'title': feed.get('title', ''),
            'id': feed.get('id', ''),
            'keywords': feed.get('keywords', ''),
            'origin_id': feed.get('originId', ''),
            'published': feed.get('published', ''),
            'stream_id': feed.get('origin', '').get('streamId', '') if feed.get('origin', '') else '',
            'author': feed.get('author', ''),
            'summary': feed.get('summary', '').get('content', '') if feed.get('summary', '') else '',
            'engagement': feed.get('engagement', 0),
            'engagementRate': feed.get('engagementRate', 0),
            'image': feed.get('visual', {}).get('url', '') if feed.get('visual', '') else '',
        })

    return feeds_data


def feeds_dictionary(feed):
    dictionary = {
        "title": feed.title,
        "feed_id": feed.feed_id,
        "keywords": list(feed.keywords.all().values_list('keyword', flat=True)),
        "stream": feed.stream,
        "origin_url": feed.origin_url,
        "published_at": str(feed.published_at),
        "updated_at": str(feed.updated_at),
        "summary": feed.summary,
        "engagement": feed.engagement,
        "is_hidden": feed.is_hidden,
        "author": feed.author.title if feed.author else '',
        "image": make_tuple(feed.image)[0] if len(make_tuple(feed.image)) >= 1 else ''
    }
    return dictionary
