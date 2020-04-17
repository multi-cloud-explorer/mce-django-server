import re

from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.views import serve
from django.urls import re_path
from django.conf import settings

def _serve(request, path, insecure=False, **kwargs):
    return serve(request, path, insecure=True, show_indexes=True, **kwargs)

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='admin:index', permanent=True)),
    #path('accounts/', include('allauth.urls')),
    path('adminmce/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('select2/', include('django_select2.urls')),
    re_path(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), _serve),
    path('mce/api/v1/', include('mce_django_app.api.urls')),
    path('django-rq/', include('django_rq.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('adminmce/doc/', include('django.contrib.admindocs.urls'))
    ] + urlpatterns


