from django.http import HttpResponse, Http404
from django.template import loader, RequestContext
import json

from quenta.storybook.models import get_story # dummy method TODO: actually fetch from DB
from quenta.storybook.models import Story

# API
def story(request, story_id): # TODO: parameter to decide which story to get
#    if request.is_ajax():
    if True:
        return HttpResponse(json.dumps('prica ' + str(story_id) + get_story()), mimetype="application/json")
    else:
        return HttpResponse('not for people...')
        # TODO: 404 or some error msg

# TODO: separate "normal" web view in the url properly - api vs. /
# HTML view
def story_html(request, story_id):
    template = loader.get_template('story.html')
    context = RequestContext(request)
    #return HttpResponse(template.render(context))
    return HttpResponse('prica broj:' + str(story_id))

#TODO: glavni home view pa se igraj s jqueryjem

def stories_list(request):
    """list all the stories"""
    template = loader.get_template('storybook.html')
    context = RequestContext(request)
    latest_stories = Story.objects.order_by('-pubdate')[:5]
    output = ', '.join([s.contentjson for s in latest_stories])
    return HttpResponse(output)
    #return HttpResponse(template.render(context))
    
