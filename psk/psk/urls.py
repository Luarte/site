from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('products.urls', namespace='products')),
    path("admin/", admin.site.urls),
    path('', include('about.urls', namespace='about')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
