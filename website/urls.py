
from django.contrib import admin
from django.urls import include, re_path as url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from feed import urls as feed_urls
from profiles import urls as profiles_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(feed_urls, namespace="feed")),
    path("profile/", include(profiles_urls, namespace="profiles")),
    url("", include("allauth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
