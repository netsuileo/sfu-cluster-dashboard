from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('app.api.urls', namespace='api')),
    url(r'^user/', include('app.user.urls', namespace='user')),
    url(r'^', include('app.home.urls', namespace='home')),
    url(r'^modules/', include('app.modules.urls', namespace='modules')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)