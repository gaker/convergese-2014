
import ttag
from django import template
from company.apps.blog.models import Post


register = template.Library()

class GetRecentPosts(ttag.helpers.AsTag):
    """
    Get recent posts

    {% get_recent_posts as recent_posts %}
    """
    def output(self, data):
        """
        return output
        """
        return Post.objects.all()


register.tag(GetRecentPosts)
