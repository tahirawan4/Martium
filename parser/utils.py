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
            'image': feed.get('visual', '').get('url', '') if feed.get('visual', '') else '',
        })

    return feeds_data
