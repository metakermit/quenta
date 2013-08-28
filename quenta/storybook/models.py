from django.db import models
import json

sample_story={'story':
                  [{'lore':'thou certainly must writeth something as a string of characters...',
                    'quest':'instanceof(_, str)'}]
              }

# TODO: use Django's ORM to get it and/or parse from Markdown
def get_story():
    return json.dumps(sample_story)

class Story(models.Model):
    name = models.CharField(max_length=200)
    contentjson = models.CharField(max_length=900) # TODO: no limit
    pubdate = models.DateTimeField('date published')

    def __unicode__(self):
        return self.name + ' - ' + self.contentjson

    def __str__(self):
        return self.__unicode__()

#TODO: app - quenta.stories ili quenta.storybook
