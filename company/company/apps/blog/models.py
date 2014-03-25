from django.conf import settings
from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    """
    Blog Posts
    """
    title = models.CharField('title', max_length=100)
    slug = models.SlugField('slug', max_length=100)
    body = models.TextField('post body',
        help_text="Write your post here, using markdown syntax.")
    date_created = models.DateTimeField('date created', default=now)
    published = models.BooleanField('published', default=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        year = self.date_created.strftime('%Y')
        month = self.date_created.strftime('%b').lower()
        day = self.date_created.strftime('%d')

        return ('blog-detail', (), {
            'year': year,
            'month': month,
            'day': day,
            'slug': self.slug
        })
