def feeds_dictionary(feed):

    dictionary = {
        "title": feed.title,
        "feed_id": feed.feed_id,
        "keywords": feed.keywords,
        "stream": feed.stream,
        "origin_url": feed.origin_url,
        "published_at": feed.published_at,
        "updated_at": feed.updated_at,
        "summary": feed.summary,
        "engagement": feed.engagement,
        "is_hidden": feed.is_hidden,
        "author": feed.author
    }
    return dictionary