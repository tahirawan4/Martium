from django.db import models


# TODO: Need to update it according to the needs
class Author(models.Model):
    title = models.CharField(max_length=100)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Stream(models.Model):
    stream_id = models.CharField(max_length=500)
    stream_title = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.stream_id


class Keyword(models.Model):
    keyword = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.keyword


class Feed(models.Model):
    title = models.CharField(max_length=200, null=True)
    feed_id = models.CharField(max_length=200)
    keywords = models.ManyToManyField(Keyword, null=True, blank=True)
    stream = models.ForeignKey(Stream, null=True)
    origin_url = models.CharField(max_length=500, null=True)
    published_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    summary = models.TextField(null=True)
    engagement = models.IntegerField(default=0)
    engagement_rate = models.FloatField(default=0.0)
    is_hidden = models.BooleanField(default=False)
    author = models.ForeignKey(Author, null=True)
    image = models.URLField(null=True, blank=True, default='')

    def __str__(self):
        return self.feed_id
