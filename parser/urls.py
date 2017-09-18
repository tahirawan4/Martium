from django.conf.urls import url
from parser.views import index,dash_board,get_categories,get_feeds

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^dashboard$', dash_board, name='dash_board'),
    url(r'^get_categories$', get_categories, name='get_categories'),
    url(r'^get_feeds/$', get_feeds, name='get_feeds'),
]
