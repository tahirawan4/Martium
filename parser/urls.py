from django.conf.urls import url
from parser.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]
