from django.conf.urls import url, include
from django.contrib import admin


from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('articles.urls')),
    url(r'^accounts/', include('accounts.urls')),
]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)