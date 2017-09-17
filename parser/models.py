from django.db import models


# TODO: Need to update it according to the needs
class Author(models.Model):
    title = models.CharField(max_length=100)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'self.title'


class Stream(models.Model):
    stream_id = models.CharField(max_length=500)
    stream_title = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.stream_id}'


class Keyword(models.Model):
    keyword = models.CharField(max_length=200)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.keyword}'


class Feed(models.Model):
    title = models.CharField(max_length=200)
    feed_id = models.CharField(max_length=200)
    keywords = models.ManyToManyField(Keyword, null=True, blank=True)
    stream = models.ForeignKey(Stream)
    origin_url = models.CharField(max_length=500)
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    summary = models.TextField()
    engagement = models.IntegerField(default=0)
    engagement_rate = models.FloatField(default=0.0)
    is_hidden = models.BooleanField(default=False)
    author = models.ForeignKey(Author)

    def __str__(self):
        return f'{self.feed_id}'
