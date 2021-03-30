from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('api/v1/', include('apps.api.v1.urls')),  # entry point to other project app urls
]

if settings.DEBUG:
    import debug_toolbar
    from rest_framework_swagger.views import get_swagger_view

    schema_view = get_swagger_view(title='Project APIs', urlconf='apps.api.v1.urls', url="/api/v1/")
    urlpatterns += [
        path('api/root/', schema_view),
        path('', RedirectView.as_view(url='/api/root/', permanent=False)),
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
