from django.conf import settings
from django.urls import include, path, re_path

from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

urlpatterns = [

    # Core
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Django Boilerplate')),

    # API (v1)
    path(r'api/', include('v1.accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
