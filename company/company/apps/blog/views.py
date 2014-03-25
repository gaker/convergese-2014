"""
Blog views
"""
from django.views import generic
from company.apps.blog.models import Post


class PostList(generic.ListView):
    """
    List of posts
    """
    template_name = 'blog/list.html'
    queryset = Post.objects.filter(published=True).select_related('author')
    context_object_name = 'posts'


class PostDetail(generic.DetailView):
    """
    Detail view.
    """
    queryset = Post.objects.filter(published=True).select_related('author')
    template_name = 'blog/detail.html'
    context_object_name = 'post'
