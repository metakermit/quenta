from django.conf.urls import patterns, url

from quenta.storybook import views

urlpatterns = patterns('',
    url(r'^(?P<story_id>\d+/)', views.story, name='story'),#+ parametar
    url(r'^(?P<story_id>\d+/html/)', views.story_html, name='story_html'),#+ parametar
    url(r'^$', views.stories_list, name='stories_list'),
)
