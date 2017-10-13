from django.conf.urls import patterns, include, url

from project.blog.views import show_article
urlpatterns = patterns('',
    # Examples:
    url(r'^(?P<path>.*)/?$', show_article, name='show_article'),
)
