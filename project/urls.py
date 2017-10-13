import os
from django.conf.urls import include, url, patterns
from django.contrib import admin
from project import settings
from welcome.views import index, health,Home,download

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view(), name='home'),                                                                                         
    url(r'^download/?$', download, name='download'),                                                                                 
    url(r'^blog/', include('blog.urls')),
]
if 1:#os.getenv("vivek_env") == "local":
    urlpatterns += patterns('', url(r'^static/(?P<path>.*)$', 'django.views.static.serve',  # NOQA                                   
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}))   
