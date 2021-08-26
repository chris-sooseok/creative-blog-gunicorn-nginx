from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.settings import DISPLAY_APPS

urlpatterns = [
    path('creative-blog-admin/', admin.site.urls),

    # user management
    path('accounts/', include('allauth.urls')),

    # main
    path('', include('main.urls')),
    
    # third party
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

for APP in DISPLAY_APPS:
    urlpatterns.append(path(f'{APP}/', include(f'{APP}.urls')))

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns