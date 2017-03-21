from django.conf.urls import url
from . import views

app_name = 'exams'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<exam_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<exam_id>[0-9]+)/evaluate/$', views.evaluate, name='evaluate'),
    url(r'^(?P<exam_id>[0-9]+)/results/$', views.results, name='results')
]
