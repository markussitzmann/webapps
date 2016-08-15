from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin

#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'djangoapps.views.home', name='home'),
#    # url(r'^blog/', include('blog.urls')),
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^filer/', include('filer.urls')),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^', include('cms.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)