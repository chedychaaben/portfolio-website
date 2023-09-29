from django.contrib import admin
from django.urls import path

#static files and media files importation
from django.conf import settings
from django.conf.urls.static import static
#static files and media files importation

from apps.portfolio import views as portfolioviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolioviews.homepage, name="homepage"),
    path('contactform/', portfolioviews.contactform, name="contactform")
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)