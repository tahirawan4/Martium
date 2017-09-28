from django.conf.urls import url,include
from django.contrib import admin
from parser.views import index,dash_board,get_categories,get_feeds,start_task,text_razor

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard$', dash_board, name='dash_board'),
    url(r'^get_categories$', get_categories, name='get_categories'),
    url(r'^get_feeds/$', get_feeds, name='get_feeds'),
    url(r'^start_task/$', start_task, name='start_task'),
    url(r'^text_razor$', text_razor, name='text_razor'),
]
